usr_input = int(input("Please enter a positive number: "))

if usr_input%2 == 0 and usr_input%3 == 0:
    print("Both")
    
elif usr_input%2 == 0 or usr_input%3 == 0:
    print("One")
else:
    print("Neither")
    
