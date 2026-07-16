# Logfire to DuckDB DLT Project

This project is designed to ingest data from Logfire and save it to DuckDB using the DLT (Data Loading Tool) framework. Below are the details regarding the project setup, usage, and structure.

## Project Structure

```
logfire-duckdb-dlt
├── .dlt
│   ├── config.toml
│   └── secrets.toml
├── pipelines
│   ├── __init__.py
│   └── logfire_to_duckdb.py
├── sources
│   ├── __init__.py
│   └── logfire.py
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd logfire-duckdb-dlt
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Copy the `.env.example` to `.env` and fill in the necessary environment variables, such as API keys and database connection strings.

4. **Configure DLT Settings**
   Update the `.dlt/config.toml` and `.dlt/secrets.toml` files with your specific configurations and sensitive information.

## Usage

To run the pipeline that ingests data from Logfire and saves it to DuckDB, execute the following command:

```bash
dlt run pipelines/logfire_to_duckdb.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- DLT framework for data loading.
- Logfire API for providing the data source.
- DuckDB for efficient data storage and querying.