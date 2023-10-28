import psycopg2
import pandas as pd 


def main():
    host = "0.0.0.0"
    database = "postgres"
    user = "postgres"
    password = "mysecretpassword"
    port = "5432"  # default port, change if necessary

    # Establish the connection
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object using the connection
    cur = conn.cursor()
    lea = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
    ussd17 = "data/ussd17.csv"

    csv_to_sql(lea, "lea", conn, cur, encoding="cp1252")
    # csv_to_sql(ussd17, "ussd17", conn, cur, encoding="uft-8")




def csv_to_sql(file_path, table_name, conn, cur, encoding):
    """Reads a csv file and creates a table in the database with the same name as the csv file.
    Args:
        file_path (str): The path to the csv file.
        table_name (str): The name of the table to be created.
        conn (psycopg2.extensions.connection): The connection object.
        cur (psycopg2.extensions.cursor): The cursor object.
    """
    df = pd.read_csv(file_path, encoding=encoding)
    df.to_sql(table_name, conn, index=False, if_exists="replace")



if __name__ == "__main__":
    main()
