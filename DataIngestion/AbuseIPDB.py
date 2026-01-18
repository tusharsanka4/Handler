from dotenv import load_dotenv
import requests
import os
import json
from datetime import datetime, timezone

load_dotenv()

API_KEY = os.getenv("AIPDB_KEY")

url = "https://api.abuseipdb.com/api/v2/blacklist"

params = {
    "confidenceMinimum": 75,
    "limit": 10
}

headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}


def fetch_data():
    response = requests.get(url, headers= headers, params=params)
    response.raise_for_status()
    return response.json()
