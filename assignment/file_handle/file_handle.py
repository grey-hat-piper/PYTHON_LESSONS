#input filename
file_name = input('Enter file name:') #file_name = 'old'

#Handling error
try:

#read existing file
    with open(f"{file_name}.txt", "r") as old:
        old_content = old.read()
        print(old_content)
        print('Done scanning!')

    #write in new file
    with open("new.txt", "w") as new:
        print('Copying into new file ...')
        new_content = new.write(old_content)
    
    #read new content
    with open("new.txt", "r") as new:
        new_content = new.read()
        print(new_content)

except FileNotFoundError:
    print("YOUR FILE DOES NOT EXIST!")