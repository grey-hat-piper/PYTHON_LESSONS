#BASIC CALCULATOR APP
first_num = float(input('Enter your first number:'))
second_num = float(input('Enter second number:'))
opp = input('Mathematical operation:')

#Addition
if opp == '+':
    print(first_num + second_num)

#Subtraction
elif opp == '-':
    print(first_num - second_num)

#Multiplication
elif opp == '*':
    print(first_num * second_num)

#Division
elif opp == '/':
    print(first_num / second_num)

#NONE
else:
    print('Operation not found!')