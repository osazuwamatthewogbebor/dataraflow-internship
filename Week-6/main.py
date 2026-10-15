import sys 
import pathlib
import pandas as pd

_p = pathlib.Path.cwd()

while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))

from db.dataraflow_db import run_query

# File for local caching incase of IP change
CSV_PATH = pathlib.Path("london_2014.csv")

def get_data(force_refresh: bool = False) -> pd.DataFrame:
    """Load data from local CSV if it exists: otherwise fetch from DB and save to CSV."""
    if CSV_PATH.exists() and not force_refresh:
        print(f"Loading cached fata from {CSV_PATH}...")
        return pd.read_csv(CSV_PATH)

    print("Local cache missing...")
    print("Querying Azure SQL Database (week0g.london_2014)...")
    df = run_query("SELECT * FROM week06.london_2014")

    # Save to local CSV for offline use
    df.to_csv(CSV_PATH, index=False)
    print(f"Successfully saved {len(df)} rows to {CSV_PATH}")



def main():
    try:
        df = get_data()

        print("\n--- Data Preview (First 5 Rows) ---")
        print(df.head())

        print(f"\n--- Shape ---\n{df.shape[0]} rows, {df.shape[1]} columns")

        print("\n--- Column Info ---")
        print(df.info())

    except Exception as e:
        print(f"\nConnection failed: {e}")
        print(f"Tip: Once IP is whitelisted, run this script once to cache the data locally")


if __name__ == "__main__":
    main()
    