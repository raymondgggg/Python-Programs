#Raymond Guevara
#018504731
#Lab 10

#2.12 Stock Transaction Program
print("2.12 Stock Transaction Program")
moneyPaid = 2000 * 40
print("The amount of money Joe paid for the stock is $" + str(moneyPaid))
brokerCommission = moneyPaid * .03
print("The Stock Broker commission is $" + str(brokerCommission))
joeSellingStock = 2000 * 42.75
newBrokerCommission = joeSellingStock *.03
print("Joe sold the stock for $" + str(joeSellingStock))
print("He paid his broker a new commission of $" + str(newBrokerCommission))
moneyLeftOver = joeSellingStock - (moneyPaid + brokerCommission + newBrokerCommission)
print("The amount of money Joe has left over is $" + str(moneyLeftOver) + " He made a profit")
print()

#3.1 Day of the week
print("3.1 Day of the week")
usrInput = int(input("Please enter a number: "))
daysOfWeek = [1,2,3,4,5,6,7]
if (usrInput in daysOfWeek):
    if (usrInput == 1):
        print("Monday")
    elif (usrInput == 2):
        print("Tuesday")
    elif (usrInput == 3):
        print("Wednesday")
    elif (usrInput == 4):
        print("Thursday")
    elif (usrInput == 5):
        print("Friday")
    elif (usrInput == 6):
        print("Saturday")
    elif (usrInput == 7):
        print("Sunday")
else:
    print("Error. Number not within range")
print()

#3.2 Area of rectangles
print("3.2 Area of Rectangles")
rectangle_length1 = int(input("Please enter the length of rectangle 1: "))
rectangle_width1 = int(input("Please enter the width of rectangle 1: "))
area1 = rectangle_length1 * rectangle_width1
rectangle_length2 = int(input("Please enter the length of rectangle 2: "))
rectangle_width2 = int(input("Please enter the width of rectangle 2: "))
area2 = rectangle_length2 * rectangle_width2
if (area1 > area2):
    print("The first input has a larger area")
elif (area2 > area1):
    print("The second input has a larger area")
else:
    print("The areas are the same")
print()

#3.13 Shipping Charges
print("3.13 Shipping Charges")
usrInput = int(input("Please enter the weight of your package: "))
if (usrInput <= 2 ):
    print("The rate per pound is $1.50")
elif (usrInput > 2 and usrInput <= 6):
    print("The rate per pound is $3.00")
elif (usrInput > 6 and usrInput <= 10):
    print("The rate per pound is $4.00")
else:
    print("The rate per pound is $4.75")




    






    


