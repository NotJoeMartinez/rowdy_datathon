import pandas as pd
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

    lea = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
    ussd17 = "data/ussd17.csv"

    csv_to_sql(lea, "lea", engine, encoding="cp1252")
    csv_to_sql(ussd17, "ussd17", engine, encoding="utf-8")


def csv_to_sql(file_path, table_name, engine, encoding):
    df = pd.read_csv(file_path, encoding=encoding)
    df.to_sql(table_name, engine, index=False, if_exists="replace")


if __name__ == "__main__":
    main()