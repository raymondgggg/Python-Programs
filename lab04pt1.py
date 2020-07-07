pet_names = ["Maple", "Mushu", "Mango", "Prince"]
user_input = input("Please enter a pet name: ")
while True:
    if (user_input == pet_names[0] or user_input == pet_names[1] or user_input == pet_names[2]
        or user_input == pet_names[3]):
        print("The pet name has been found, it is " + user_input)
        break
    else:
        print("The name was not found.")
        user_input2 = input('Please enter name again: ')
        if (user_input2 == pet_names[0] or user_input2 == pet_names[1] or user_input2 == pet_names[2]
        or user_input2 == pet_names[3]):
            print("The pet name has been found, it is " + user_input)
            break
        else:
            print("The name is not found")
            break
        
        
    
    
