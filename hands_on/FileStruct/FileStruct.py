#print("File Structure")
# x = 120
# y = 200
# z = 300
# def add(x, y, z):
#     return x + y + z
# print(add(x, y, z))   

# with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
#     print(file.read())

# file = open('readme.md', 'w', encoding='utf-8')
# file.write('Welcome to PLP Academy.\n')
# print('File created successfully.')
# file.close()

# Append "welcome to PLP" to readme.md
with open("readme.md", "a", encoding="utf-8", errors="ignore") as file:
    file.write("\nwelcome to PLP")
# print("File structure module loaded successfully.")# Now read and print the updated file
with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
    print(file.read())





