import openai
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def answer_question(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful financial analyst."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def analyze_financial_data(financial_data):
    prompt = f"Analyze the following financial data: {financial_data}. Provide insights based on this data."
    return answer_question(prompt)
