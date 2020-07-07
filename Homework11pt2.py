#Raymond Guevara
#Homework 11 part 2
#018504731

#Programming exercise 4.4 Distance traveled
print("Problem 4.4")
speed = int(input("What is the speed of the vehical in mph? "))
hrs = int(input("How many hours has it traveled? "))
for i in range(1,hrs + 1):
    distance_traveled = speed * i
    print(str(i) + "\t" + str(distance_traveled))
print()

#Programming exercise 4.10 Tuition increase
print("Problem 4.10")
tuition = 8000
for i in range(1,5+1):
    increase_amount = tuition * 0.03
    tuition += increase_amount
    print("Year " + str(i) + " tuition is $" + str("%.2f"%tuition))
    
    
