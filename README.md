# Cloud-Linked Internet Performance Tracker

This project is a Python-based tool that monitors local network speed, tracks data usage, and logs the data into a Google Sheet for easy access.

## Features

- Monitors download and upload speeds
- Logs ping (latency)
- Tracks data usage (sent and received)
- Sends the results to Google Sheets

## Setup Instructions

1. **Clone the Repository**

git clone https://github.com/mayam4433/Cloud-Linked-Internet-Performance-Tracker.git
cd Cloud-Linked-Internet-Performance-Tracker


2. **Install Required Libraries**

pip install -r requirements.txt


3. **Set Up Google Cloud**

- Create a Google Cloud project
- Enable the Google Sheets API and Google Drive API
- Create a service account and download the JSON key file
- Place the JSON file in the same folder as the script

4. **Share Your Google Sheet**

- Create a Google Sheet
- Share it with your service account’s email (Editor access)

5. **Edit the Script**

In `network_monitor_to_sheets.py` update:

SERVICE_ACCOUNT_FILE = 'your-json-file.json'
SPREADSHEET_NAME = 'Your Google Sheet Name'


6. **Run the Script**

python network_monitor_to_sheets.py

markdown
Copy
Edit

## Notes

- The JSON key file should not be uploaded to GitHub (it's already ignored by .gitignore)
- Make sure you have Python installed
