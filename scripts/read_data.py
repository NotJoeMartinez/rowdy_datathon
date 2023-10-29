
# data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
# f = open(data_path, "r" , encoding = "cp1252")
# counter = 0

# for x in f :
#     counter = counter + 1


# import pandas as pd
# import csv

# data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
# data_path = "data/superiorfox_all_2310242047.csv"

# data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/High School Equivalency (GED).csv"
# dataframe = pd.read_csv(data_path, encoding="cp1252")

# column_headers = dataframe.columns.tolist()
# print("LEA Characteristics.csv")
# print(column_headers)

# import pandas as pd

# data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
# lea_chars = pd.read_csv(data_path, encoding="cp1252")

# for index, row in lea_chars.iterrows():
#     row_list = row.tolist()
#     print(row_list)

import pandas as pd

def get_lea():
    data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"
    lea_chars = pd.read_csv(data_path, encoding="cp1252")
    leaid_list = lea_chars['LEAID'].tolist()
    return leaid_list

def get_edge():
    data_path = "./data/EDGE_GEOCODE_PUBLICLEA_1718/EDGE_GEOCODE_PUBLICLEA_1718/EDGE_GEOCODE_PUBLICLEA_1718.csv"
    lea_chars = pd.read_csv(data_path)
    leaid_list = lea_chars['LEAID'].tolist()
    return leaid_list



lea = get_lea()
edge = get_edge()

print(f"lea: {len(lea)}")
print(f"edge: {len(edge)}")

missing_from_lea = []

for x in edge:
    if x not in lea:
        missing_from_lea.append(x)


# for x in missing_from_lea:
#     print(x)

print(f"missing from lea: {len(missing_from_lea)}")