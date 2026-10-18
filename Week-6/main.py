import sys 
import pathlib
import pandas as pd

_p = pathlib.Path.cwd()

while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))

from db.dataraflow_db import run_query

# File for local caching incase of IP change
def get_table(table_name: str, schema: str = "week06", force_refresh: bool = False) -> pd.DataFrame:
    """Load data from local CSV if it exists; otherwise fetch from DB and save to CSV.
    If the online DB is unreachable, automatically falls back to the local CSV copy.
    """
    csv_path = pathlib.Path(f"{table_name}.csv")
    if csv_path.exists() and not force_refresh:
        print(f"Loading cached data from {csv_path}...")
        return pd.read_csv(csv_path)

    try:
        print(f"Querying online Azure SQL Database ({schema}.{table_name})...")
        df = run_query(f"SELECT * FROM {schema}.{table_name}")
        df.to_csv(csv_path, index=False)
        print(f"Successfully saved {len(df)} rows to {csv_path}")
        return df
    except Exception as e:
        print(f"Online database query failed: {e}")
        if csv_path.exists():
            print(f"Falling back to local copy at {csv_path}...")
            return pd.read_csv(csv_path)
        raise RuntimeError(f"Online database unavailable and no local copy found for {table_name}.") from e

def get_data(force_refresh: bool = False) -> pd.DataFrame:
    """Load London 2014 data from local CSV if it exists; otherwise fetch from DB and save to CSV."""
    return get_table("london_2014", force_refresh=force_refresh)



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
    