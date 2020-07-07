#Raymond Guevara
#018504731
#Homework 12
print("Problem 4.7")
n_days = int(input("Please enter the number of days worked: "))
running_total = 0
pay = .01
for i in range(1, n_days +1):
    running_total += pay
    print("Day " + str(i) + "\t" + "$" + str("%.2f"%pay))
    pay *= 2
print("The total is $" + str("%.2f"%running_total))
print()

print("problem 4.8")
loop_condition = 1
count = 0
while loop_condition ==1:
    n = int(input("Enter positive number (negative to exit out): "))
    if n > 0:
        count += n
    elif n < 0:
        loop_condition = 0
print(count)
            



