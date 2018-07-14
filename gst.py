import math
price = 1000
quantity = int(input("enter the quantity of product"))
discount = 20
bill = (price*quantity)-(price*(discount/100))
total = bill + (18/100)
print(total)
