import re
from bs4 import BeautifulSoup

def clean_text(text):
    try:
        cleaned_text = BeautifulSoup(text, 'html.parser').get_text()
    except Exception as e:
        try:
            cleaned_text = BeautifulSoup(text, 'lxml').get_text()
        except Exception as e:
            cleaned_text = ''
    cleaned_text = re.sub(r'[^\w\s.,]', '', cleaned_text)
    return cleaned_text.strip()

def extract_financial_info(text):
    financial_data = {}

    # Define regex patterns for common financial metrics
    financial_patterns = {
        'revenue': r'(?:total\s+)?revenue(?:\s+in\s+millions)?\s+([\d,.]+)',
        'net_income': r'net\s+income(?:\s+in\s+millions)?\s+([\d,.]+)',
        'total_assets': r'total\s+assets(?:\s+in\s+millions)?\s+([\d,.]+)',
        'total_liabilities': r'total\s+liabilities(?:\s+in\s+millions)?\s+([\d,.]+)'
        # Add more patterns for other metrics as needed
    }

    # Clean text content
    cleaned_text = clean_text(text)

    # Extract financial metrics using regex from cleaned text
    for metric, pattern in financial_patterns.items():
        match = re.search(pattern, cleaned_text, re.IGNORECASE)
        if match:
            try:
                financial_data[metric] = float(match.group(1).replace(',', ''))
            except ValueError:
                financial_data[metric] = None
        else:
            financial_data[metric] = None

    return financial_data
