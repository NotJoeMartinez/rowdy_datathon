

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

    enrollment_data = get_enrollment_data(cur, conn, lea_ids)

    combined_data = combine_enrollment_with_poverty(cur, conn, enrollment_data) 
    print(combined_data)

    for i in combined_data[0:10]:
        print(i)


    # print(lea_ids[0:10])
    # print(ussd17_ids[0:10])

    # 
    has_data = []
    for i in ussd17_ids:
        if i in lea_ids:
            has_data.append(i)
    
    print(f"Number of LEAs with data: {len(has_data)}")

    print(has_data[0:10])

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
            tables.append(i[0])
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

        tables.append(full_id)

    return tables



def get_enrollment_data(cur, conn, ids):

    # Connection parameters

    cur.execute("""
    SELECT "LEAID", "LEA_NAME", "LEA_ENR" FROM lea
    """)

    # Fetch all results
    res = cur.fetchall()

    tables = []
    for row in res:
        if row[0] in ids:

            tables.append(row)


    return tables


def combine_enrollment_with_poverty(cur, conn, enrollment_data):
    
    combined_data = []

    cur.execute("""
        SELECT "State FIPS Code","District ID","Estimated number of relevant children 5 to 17 years old in poverty who are related to the householder"
        from ussd17
    """)

    res = cur.fetchall()


    for row in enrollment_data:
        lae_id = str(row[0])

        for i in res:
            if lae_id == str(i[0]) + str(i[1]):
                print(f"Found match: {lae_id}")
                combined_data.append(row + (i[2],))


    # for row in res:
    #     for i in enrollment_data:
    #         if row[0] + row[1] == i[0]:
    #             combined_data.append(i + (row[2],))

    return combined_data

if __name__ == "__main__":
    main()