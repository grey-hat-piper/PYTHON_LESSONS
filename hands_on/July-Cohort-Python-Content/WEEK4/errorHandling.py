try:
    file = open("jsMummies_Contacts.pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")



# file = open("jsMummies_Contacts.pdf", "r")
# content = file.read()
# print(content)