
import psycopg2

#  docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -v /path/on/host:/var/lib/postgresql/data -d postgres
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

# Execute a simple query
# cur.execute("SELECT version();")
# version = cur.fetchone()
# print(f"Database Version: {version[0]}")

cur.execute("""
CREATE TABLE IF NOT EXISTS lea (
  LEA_STATE TEXT,
  LEA_STATE_NAME TEXT,
  LEAID TEXT,
  LEA_NAME TEXT,
  LEA_ADDRESS TEXT,
  LEA_CITY TEXT,
  LEA_ZIP TEXT,
  CJJ TEXT,
  LEA_ENR INTEGER,
  LEA_ENR_NONLEAFAC INTEGER,
  LEA_SCHOOLS INTEGER,
  LEA_CRCOORD_SEX_IND TEXT,
  LEA_CRCOORD_RAC_IND TEXT,
  LEA_CRCOORD_DIS_IND TEXT,
  LEA_CRCOORD_SEX_FN TEXT,
  LEA_CRCOORD_SEX_LN TEXT,
  LEA_CRCOORD_SEX_PH TEXT,
  LEA_CRCOORD_SEX_EM TEXT,
  LEA_CRCOORD_RAC_FN TEXT,
  LEA_CRCOORD_RAC_LN TEXT,
  LEA_CRCOORD_RAC_PH TEXT,
  LEA_CRCOORD_RAC_EM TEXT,
  LEA_CRCOORD_DIS_FN TEXT,
  LEA_CRCOORD_DIS_LN TEXT,
  LEA_CRCOORD_DIS_PH TEXT,
  LEA_CRCOORD_DIS_EM TEXT,
  LEA_DESEGPLAN TEXT,
  LEA_HBPOLICY_IND TEXT,
  LEA_HBPOLICYURL_IND TEXT,
  LEA_HBPOLICY_URL TEXT,
  LEA_ECE_IND TEXT,
  LEA_ECE_NONIDEA TEXT,
  LEA_PS_IND TEXT,
  LEA_PS_FULLDAYFREE TEXT,
  LEA_PS_FULLDAYCOST TEXT,
  LEA_PS_PARTDAYFREE TEXT,
  LEA_PS_PARTDAYCOST TEXT,
  LEA_PSENR_NONIDEA_A3 TEXT,
  LEA_PSENR_NONIDEA_A4 TEXT,
  LEA_PSENR_NONIDEA_A5 TEXT,
  LEA_PSENR_A2 INTEGER,
  LEA_PSENR_A3 INTEGER,
  LEA_PSENR_A4 INTEGER,
  LEA_PSENR_A5 INTEGER,
  LEA_PSELIG_ALL TEXT,
  LEA_PSELIG_IDEA TEXT,
  LEA_PSELIG_TITLEI TEXT,
  LEA_PSELIG_LOWINC TEXT,
  LEA_KG_IND TEXT,
  LEA_KG_FULLDAYFREE TEXT,
  LEA_KG_FULLDAYCOST TEXT,
  LEA_KG_PARTDAYFREE TEXT,
  LEA_KG_PARTDAYCOST TEXT
);



CREATE TABLE IF NOT EXISTS ussd17 (
    STATE_POSTAL_CODE TEXT, 
    STATE_FIPS_CODE TEXT,
    DISTRICT_ID TEXT,
    DISTRICT_NAME TEXT,
    ETP INTEGER, 
    ETP_5_17 INTEGER, 
    NUM_UNDER_POVERTY INTEGER 
);

""")

# Close the cursor and connection
cur.close()
conn.commit()
conn.close()