import psycopg2

host = "0.0.0.0"
database = "postgres"
user = "postgres"
password = "mysecretpassword"
port = "5432"  


conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor object using the connection
cur = conn.cursor()

cur.execute("""
   SELECT "tract", "Household_Income_at_Age_35_rP_gP_pall" FROM "shown_tract_kfr_rP_gP_pall"
""")


# Fetch all results
tract_income = cur.fetchall()

cur.execute("""
            SELECT * FROM "grf17_lea_tract"
            """)
tract_to_leaid = cur.fetchall()



track_to_leaid = []

for row in tract_income:
    leaid = ""
    tract = row[0]
    income = row[1]
    
    for j in tract_to_leaid:
        sub_track = j[2] 
        if tract == sub_track:
            leaid = j[0]
            break


    if leaid != "":
        track_to_leaid.append((leaid, tract, income))

cur.execute("""
SELECT "LEAID", "LEA_NAME", 
       "TOT_ALGPASS_G08_M", 
       "TOT_ALGPASS_G08_F", 
       ("TOT_ALGPASS_G08_M" + "TOT_ALGPASS_G08_F") AS "TOTAL_ALGPASS_G08"
FROM "Algebra_I" 
WHERE 
    "TOT_ALGPASS_G08_M" > 0
AND 
    "TOT_ALGPASS_G08_F" > 0
ORDER BY 
    "TOTAL_ALGPASS_G08" DESC;
            """)

algebra_passers = cur.fetchall()



for row in track_to_leaid:
    leaid = str(row[0])
    tract = row[1]
    income = row[2]
    
    for j in algebra_passers:

        sub_leaid = j[0]

        num_passers = j[4]

        if leaid == sub_leaid:
            print(leaid, tract, income, num_passers) 

            break


cur.close()
conn.close()
