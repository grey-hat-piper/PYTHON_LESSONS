#QUESTION 1
def calculate_discount(price, discount_percent):
    '''Calculates final price after applying discount'''
    if discount_percent >= 20 :
        discount_price = price * (discount_percent/100)
        final_price = price - discount_price
        return final_price
    else :
        return price
    
#QUESTION 2
price = int(input('Enter the price:'))
discount_percent = int(input('Enter the discount percentage:'))

#output
print(calculate_discount(price, discount_percent))