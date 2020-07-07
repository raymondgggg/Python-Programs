#Raymond Guevara
#Lab 11 part 2
#018504731

#4.3 Budget Analysis
print("Part 1: 4.3 Budget Analysis")
usr_input = int(input("Please enter your budget amount: "))#Asks user for amount they have budgeted for a month
loop_condition = 0 
count = 0
while loop_condition == 0:
    print("Please enter your expenses: ", end = "")
    expenses = int(input())
    count += expenses #adds the monthly expenses to the count
    prompt = input("Do you have more expenses? (y/n): ")
    if prompt == 'n':
        loop_condition = 1
        print("Your monthly expenses totaled to $" + str(count)+ ",", end = "")
        print(" your budget was $" + str(usr_input) + ".")
        if count > usr_input:
            print("You are over budget.")
        elif count < usr_input:
            print("You are under the budget.")
        else:
            print("You broke even.")
print()

#Lab: Problem 2 
print("Part 2")
loop_condition = 0
count = 0
n = 1
while loop_condition == 0: #Numbers divisible by 5 in range 
    summation = 5*n     #General series expression
    n += 1
    count += summation
    if n > 20: 
        loop_condition = 1
count += 1 + 101 # adding numbers in beginning and end of range
print(count)
print()

#Lab: Problem 3

print("Part 3")
loop_condition = 0
count = 0
n = 1 #variable for general expression
while loop_condition == 0:
    summation = 4 + 3*(n - 1) #general series expression
    n += 1
    count += summation
    if n > 333: 
        loop_condition = 1
count += 1 + 1001         #Numbers at the beginning of the interval
print(count)




    
    


        
    
    
    
