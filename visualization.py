import matplotlib.pyplot as plt
import streamlit as st

def visualize_financial_metrics(ticker, processed_financial_data):
    financial_metrics = ['revenue', 'net_income', 'total_assets', 'total_liabilities']

    if ticker in processed_financial_data:
        years_data = processed_financial_data[ticker]

        years = sorted(years_data.keys())
        num_metrics = len(financial_metrics)

        fig, axes = plt.subplots(num_metrics, 3, figsize=(18, 12))
        fig.suptitle(f"Financial Metrics Over Years for {ticker}", fontsize=16)

        for i, metric in enumerate(financial_metrics):
            metric_values = []
            for year in years:
                financial_info = years_data[year]['financial_info']
                metric_value = financial_info.get(metric, None)
                metric_values.append(metric_value)

            axes[i, 0].plot(years, metric_values, marker='o', linestyle='-', color='b')
            axes[i, 0].set_ylabel(metric.capitalize())
            axes[i, 0].set_xlabel("Year")
            axes[i, 0].grid(True)

            jitter_years = [year + 0.2 * (i - 1.5) for year in years]
            axes[i, 1].scatter(jitter_years, metric_values, color='g', alpha=0.7)
            axes[i, 1].set_ylabel(metric.capitalize())
            axes[i, 1].set_xlabel("Year (with jitter)")
            axes[i, 1].grid(True)

            assets = [years_data[year]['financial_info'].get('total_assets', 0) or 0 for year in years]
            liabilities = [years_data[year]['financial_info'].get('total_liabilities', 0) or 0 for year in years]
            axes[i, 2].bar(years, assets, color='b', label='Total Assets')
            axes[i, 2].bar(years, liabilities, color='r', label='Total Liabilities', bottom=assets)
            axes[i, 2].set_ylabel("Amount")
            axes[i, 2].set_xlabel("Year")
            axes[i, 2].legend()
            axes[i, 2].grid(True)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        st.pyplot(fig)

    else:
        st.write(f"No data found for ticker: {ticker}")
