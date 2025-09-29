import pandas as pd

try:
    # Read the Excel file (sheet1 by default)
    df = pd.read_excel("Book1.xlsx", sheet_name=0, engine="openpyxl")
    
    # Display the contents
    print(df)
except FileNotFoundError:
    print("File not found. Please check the file name and path.")
except Exception as e:
    print("Error:", e)
