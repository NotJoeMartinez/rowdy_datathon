data_path = "data/2017-18-crdc-data/2017-18 Public-Use Files/Data/LEA/CRDC/CSV/LEA Characteristics.csv"

with open(data_path, "r", encoding="cp1252") as f:
    content = f.read()
    
# Split the content by lines
lines = content.split("\n")

# Keep track of multi-line fields
inside_quotes = False
multi_line_data = ""

for line in lines:
    # Count the number of double quotes in the line
    num_quotes = line.count('"')
    
    # If there's an odd number of quotes, we toggle the inside_quotes flag
    if num_quotes % 2 != 0:
        inside_quotes = not inside_quotes
    
    # If we're inside a multi-line field, accumulate the line; otherwise, reset
    if inside_quotes:
        multi_line_data += line + "\n"
    else:
        if multi_line_data:
            multi_line_data += line
            print("Multi-line Row:\n", multi_line_data)
            multi_line_data = ""

