#Error Handling in Python
# try: 
#     with open("readme.txt", "r",) as file:
#         data = file.read()
# except FileNotFoundError:
#     print("File not found. Please check the file path.")
# Error Handling in Python for Excel file
try:
    with open("Book1.xlsx", "rb") as f:   # open in binary mode
        content = f.read()
        print("Excel file opened successfully. Size:", len(content), "bytes")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
