from typing import Any, Dict
import requests

LOGFIRE_API_URL = "https://api.logfire.com/data"  # Replace with the actual Logfire API endpoint

def fetch_logfire_data(params: Dict[str, Any]) -> Any:
    response = requests.get(LOGFIRE_API_URL, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def extract_data() -> Any:
    params = {
        # Add necessary parameters for the Logfire API request
    }
    data = fetch_logfire_data(params)
    print("data: ", data)
    return data