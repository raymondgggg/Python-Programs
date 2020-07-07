#Lab 09 programming exercises#
#Raymond Guevara#
#018504731#

# 2.1 Personal information
print("2.1 personal information")
print("""Name: Raymond Guevara
Location: 5054 east warren dr, Lancaster, California, 96552
Phone: 818-456-7848
Major: Computer Science""")

print()

# 2.5 Distance Traveled
print('2.5 Distance Traveled')
speed = 70 #mph
distance1 = 70 * 6
distance2 = 70 * 10
distance3 = 70 * 15
print('In 6 hours the car will travel ', end='')
print(distance1,end ='')
print(' miles')
print('In 10 hours the car will travel ', end='')
print(distance2, end='')
print(' miles')
print('In 15 hours the car will travel ', end= '')
print(distance3,end = '')
print(' miles')


print()

# 2.6 Sales tax
print("2.6 Sales tax")
purchase_total = float(input("Please enter the total of the purchase: "))
print("$" + str('%.2f'%purchase_total)+ " is the purchase total")
state_sales_tax = purchase_total * .05
print("$" + str('%.2f'%state_sales_tax) + " is the state sales tax")
country_sales_tax = purchase_total *.025
print("$" + str('%.2f'%country_sales_tax) + " is the country sales tax")
total_sales_tax = purchase_total * .075
print("$" + str('%.2f'%total_sales_tax) + " is the total sales tax")
total_of_sale = purchase_total + total_sales_tax
print("$" + str('%.2f'%total_of_sale) + " is the total of the sale")




