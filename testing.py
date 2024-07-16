from helpers import get_postgres_engine
from extract import run_extraction
from load import load_csv_to_postgres



engine = get_postgres_engine()

run_extraction()

load_csv_to_postgres('goalbet.csv', 'goalbet', engine, 'STG')