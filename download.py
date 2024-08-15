import os
from sec_edgar_downloader import Downloader

def download_10k_filings(ticker, after_date, before_date):
    base_dir = os.getcwd()
    target_dir = os.path.join(base_dir, "sec-edgar-filings", "10-K", ticker)

    # Initialize the downloader
    dl = Downloader("VIT", "akanksha.dhar2020@vitstudent.ac.in")

    try:
        # Download the 10-K filings for the given ticker within the date range
        dl.get("10-K", ticker, after=after_date, before=before_date)
        print(f"Downloading 10-K filings for {ticker} between {after_date} and {before_date}...")
        print(f"Successfully downloaded 10-K filings for {ticker} between {after_date} and {before_date}")
        return True  # Return True if download is successful
    except Exception as e:
        print(f"Error downloading 10-K filings for {ticker}: {e}")
        return False  # Return False if download fails
