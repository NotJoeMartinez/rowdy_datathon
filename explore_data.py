

import psycopg2

def main():
    # Connection parameters
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


    lea_ids = get_lea_ids(cur, conn)
    ussd17_ids = get_ussd17_ids(cur, conn)


    print(lea_ids[0:10])
    print(ussd17_ids[0:10])

    # 
    has_data = []
    for i in ussd17_ids:
        if i in lea_ids:
            has_data.append(i)
    
    print(f"Number of LEAs with data: {len(has_data)}")

    cur.close()
    conn.close()


def get_lea_ids(cur, conn):

    # Connection parameters
    host = ""
    cur.execute("""
    SELECT "LEAID" FROM lea
    """)

    # Fetch all results
    res = cur.fetchall()

    tables = []
    for i in res:
        if i[0].isnumeric():
            tables.append(int(i[0]))
        else:
            continue

    return tables

def get_ussd17_ids(cur, conn):

    # Connection parameters
    host = ""
    cur.execute("""
    SELECT "State FIPS Code", "District ID"  FROM ussd17
    """)

    # Fetch all results
    res = cur.fetchall()

    tables = []

    for i in res:
        full_id = str(i[0]) + str(i[1])

        tables.append(int(full_id))


    return tables

if __name__ == "__main__":
    main()