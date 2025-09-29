# file = open("./WEEK4/jsMummies_Contacts.pdf", "w")
# file.write("JsMammie1, JsMammie2, JsMammie3\n")


# Appending content to a file
# file = open("./WEEK4/jsMummies_Contacts.pdf", "a")
# file.write("Ooh my Sheilla, I love you so much")


# Reading content from a file

# file = open("./WEEK4/jsMummies_Contacts.pdf", "r")
# content = file.readline()
# print(content)



# Reading image content from a file
image_file = open("./WEEK4/kafka.png", "rb")
image_data = image_file.read()
print(image_data[:100])