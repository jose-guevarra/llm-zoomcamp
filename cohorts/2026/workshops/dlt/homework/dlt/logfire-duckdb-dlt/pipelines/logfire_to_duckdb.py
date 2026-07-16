from dlt import pipeline, source
import duckdb
import requests
from typing import Any, Dict

LOGFIRE_API_URL = "https://api.logfire.com/data"  # Replace with the actual Logfire API endpoint


@pipeline
def logfire_to_duckdb():
    data = fetch_logfire_data()
    load_to_duckdb(data)

@source
def fetch_logfire_data(params: Dict[str, Any]) -> Any:
    response = requests.get(LOGFIRE_API_URL, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def load_to_duckdb(data):
    # Logic to save data to DuckDB
    conn = duckdb.connect('local_duckdb.db')
    conn.execute("CREATE TABLE IF NOT EXISTS logfire_data AS SELECT * FROM data")
    conn.execute("INSERT INTO logfire_data SELECT * FROM data")
    conn.close()