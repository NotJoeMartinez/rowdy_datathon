import pandas as pd
import glob
from sqlalchemy import create_engine


def main():
    host = "0.0.0.0"
    database = "postgres"
    user = "postgres"
    password = "mysecretpassword"
    port = "5432"  # default port, change if necessary

    # Create an SQLAlchemy connection string
    conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    # Establish the connection using SQLAlchemy's create_engine
    engine = create_engine(conn_str)

    valid_csvs = glob.glob("/*.csv") 
    valid_csvs = glob.glob(f"data/GRF17/GRF17/csv/**/*.csv", recursive=True)

    for csv in valid_csvs:
        table_name = csv.split("/")[-1].split(".")[0]
        table_name = table_name.replace(" ", "_").replace("-", "_")
        csv_to_sql(csv, table_name, engine, encoding="cp1252")


    
    # hmda = "data/parts_hmda_2017_nationwide_all-records_labels/part_1_of_3_hmda_2017_nationwide_all-records_labels.csv"
    # hmda = "data/parts_hmda_2017_nationwide_all-records_labels/full_hmda_2017_records_labels.csv"


    # csv_to_sql(hmda, "hmda", engine, encoding="utf-8")

# def csv_to_sql(file_path, table_name, engine, encoding, chunk_size=50000):  # setting default chunk size to 50,000 rows
    # Calculate total rows for progress tracking
    # total_rows = sum(1 for _ in open(file_path, 'r', encoding=encoding)) - 1  # -1 to exclude header
    # num_chunks = (total_rows // chunk_size) + 1

    # Use an iterator to read the file in chunks
    # iter_csv = pd.read_csv(file_path, encoding=encoding, iterator=True, chunksize=chunk_size)
    
    # for i, chunk in enumerate(iter_csv):
    #     print(f"Processing chunk {i + 1} of {num_chunks}")
    #     chunk.to_sql(table_name, engine, index=False, if_exists="replace" if i == 0 else "append")
    #     print(f"Finished chunk {i + 1} of {num_chunks}")

    # print("Upload complete.")

def csv_to_sql(file_path, table_name, engine, encoding):
    df = pd.read_csv(file_path, encoding=encoding)
    df.to_sql(table_name, engine, index=False, if_exists="replace")


if __name__ == "__main__":
    main()