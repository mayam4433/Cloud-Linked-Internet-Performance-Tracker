import speedtest
import psutil
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# --- Google Sheets Setup ---
SERVICE_ACCOUNT_FILE = 'your-service-account-file.json'  # <-- UPDATE THIS with your JSON file
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

SPREADSHEET_NAME = 'Network Monitor Data'  # <-- UPDATE this with your own Google Sheet name

# Authenticate
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open(SPREADSHEET_NAME).sheet1

def run_speed_test():
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000  # Mbps
    upload = st.upload() / 1_000_000      # Mbps
    ping = st.results.ping
    return round(download, 2), round(upload, 2), ping

def get_data_usage():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent / (1024 ** 2)  # MB
    recv = counters.bytes_recv / (1024 ** 2)  # MB
    return round(sent, 2), round(recv, 2)

def log_to_google_sheets(data_row):
    sheet.append_row(data_row)
    print("Data logged to Google Sheet!")

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    download, upload, ping = run_speed_test()
    sent, recv = get_data_usage()
    data_row = [timestamp, download, upload, ping, sent, recv]

    print(f"Logging: {data_row}")
    log_to_google_sheets(data_row)
