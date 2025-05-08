# Cloud-Linked Internet Performance Tracker

This is a Python-based tool that monitors local network speed, tracks data usage, and logs the results to a Google Sheet. It collects download speed, upload speed, ping (latency), and data usage statistics, and sends them to a Google Sheet using Google Cloud’s API.

To set it up, first clone the repository using:

git clone https://github.com/mayam4433/Cloud-Linked-Internet-Performance-Tracker.git
cd Cloud-Linked-Internet-Performance-Tracker

Next, install the required Python libraries:

pip install -r requirements.txt

Before running the script, set up your Google Cloud project. Enable the Google Sheets API and the Google Drive API. Create a service account and download the JSON key file. Save this JSON file in the same folder as the script.

Create a Google Sheet where the data will be logged. Share the sheet with your service account’s email and give it Editor access.

In the script file network_monitor_to_sheets.py, update these lines with your own details:

SERVICE_ACCOUNT_FILE = 'your-json-file.json'
SPREADSHEET_NAME = 'Your Google Sheet Name'

Once that’s set up, you can run the script with:

python network_monitor_to_sheets.py

This will log the network performance data directly into your Google Sheet. Make sure not to upload your JSON key file to GitHub, as it contains sensitive information.

