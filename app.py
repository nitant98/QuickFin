import streamlit as st
import os
import re
from dotenv import load_dotenv
from download import download_10k_filings
from processing import extract_financial_info
from analysis import configure_gemini, answer_question, analyze_financial_data, answer_complex_question
from visualization import visualize_financial_metrics
import google.generativeai as genai

# Configure the Gemini API
load_dotenv()
configure_gemini(os.getenv('gemini_api'))

def login():
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image("QuickFin.png", width=350)

    st.markdown("<p style='color:purple; text-align: center;'>Welcome to <b>QuickFin</b>! Please login to continue.</p>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")


def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        st.sidebar.image("QuickFin.png", use_column_width=True)
        st.sidebar.title("Input Parameters")

        ticker = st.sidebar.text_input("Enter company ticker: (Press Enter once done)")
        after_date = st.sidebar.text_input("Enter After Date (YYYY-MM-DD)", "1995-01-01")
        before_date = st.sidebar.text_input("Enter Before Date (YYYY-MM-DD)", "1998-01-01")

        #if st.sidebar.button("Start Analysis"):
        st.write(f"Download started for {ticker} from {after_date} to {before_date}")

        if download_10k_filings(ticker, after_date, before_date):
            st.write("Download successful!")
            
            if ticker:
                base_dir = os.getcwd()
                target_dir = os.path.join(base_dir, "sec-edgar-filings", ticker)
                processed_financial_data = {}
                longdir = os.path.join(target_dir, '10-K')

                st.write("Extracting financial data for analysis and generating insights...")

                for company_dir in os.listdir(longdir):
                    company_path = os.path.join(longdir, company_dir)
                    
                    if os.path.isdir(company_path):
                        year_match = re.search(r'-(\d{2})-', company_dir)
                        if year_match:
                            year_suffix = year_match.group(1)
                            year = 2000 + int(year_suffix) if int(year_suffix) <= 23 else 1900 + int(year_suffix)

                            for file in os.listdir(company_path):
                                if file.endswith('.txt'):
                                    with open(os.path.join(company_path, file), 'r', encoding='utf-8') as f:
                                        text_content = f.read()
                                        financial_info = extract_financial_info(text_content)
                                        financial_insights = analyze_financial_data(financial_info)
                                        
                                        if ticker not in processed_financial_data:
                                            processed_financial_data[ticker] = {}
                                        processed_financial_data[ticker][year] = {
                                            'financial_info': financial_info,
                                            'financial_insights': financial_insights
                                        }
                                    break

                if ticker in processed_financial_data:
                    st.header(f"Financial Details for Ticker: {ticker}")
                    financial_metrics = ['revenue', 'net_income', 'total_assets', 'total_liabilities']
                    table_data = [["Year"] + financial_metrics + ["Financial Insights"]]

                    for year, data in sorted(processed_financial_data[ticker].items()):
                        financial_info = data['financial_info']
                        financial_insights = data.get('financial_insights', None)
                        row_data = [year] + [financial_info.get(metric, None) for metric in financial_metrics] + [financial_insights if financial_insights else None]
                        table_data.append(row_data)

                    st.table(table_data)

                st.header(f"Financial Visualizations for Ticker: {ticker}")
                visualize_financial_metrics(ticker, processed_financial_data)

                st.header("Interesting Observations in Financial Analysis")
                answer_obs = answer_question(prompt=f"Is there any sharp decline or increase in any year between 1995-2023 in the financial metrics of {ticker}? What insight do we get from that?")
                st.write(answer_obs)

                st.header(f"Overall Insights and Analysis of {ticker}")
                overall_insights = answer_question(prompt=f"What insights do you get from the financial metrics in the 10k filings of {ticker} from 1995 to 2023?")
                st.write(overall_insights)

                st.header("Ask a question")
                prompt_ask = st.text_input("Enter your question related to the financial analysis")
                if prompt_ask:
                    st.write(f"Processing answer for the question: {prompt_ask}")
                    answer_ask = answer_question(prompt_ask)
                    st.write(answer_ask)

            else:
                st.write(f"No data found for ticker: {ticker}")

        else:
            st.write(f"Failed to download 10-K filings for {ticker}")


if __name__ == "__main__":
    main()
