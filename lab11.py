#Problem 3.18
print("3.18")
usr_input = input('Is anyone in your party a vegetarian?(yes/no)')
usr_input2 = input('Is anyone in your party vegan?(yes/no)')
usr_input3 = input('Is anyone in your party gluten-free?(yes/no)')
print()
print("Here are your choices: ")

if usr_input == 'yes':
    ##main street, corner, mama, the chef
    if usr_input2 == 'yes':
        ## corner cafe, chefs kictchen
        if usr_input3 == 'yes':
            ##coner, chef
            print("Corner cafe")
            print("The Chef's Kitchen")
        elif usr_input3 == 'no':
            print("None based off of yes for vegetarian and vegan, and no for gluten-free.")
            
            
    elif usr_input2 == 'no':
        ## mama, main street
        if usr_input3 == 'yes':
            ## main
            print("Main Street Pizza Co")
        elif usr_input3 == 'no':
            # mama
            print("Mamma's Fine Italian")
                        
else:
    print("Joe's Burgers")

print()
print("3.8")
usr_input = int(input("How many people will be attending the cook out? "))
usr_input2 = int(input("How many hot dogs per person? "))

hot_dogPkgs_needed = (usr_input*usr_input2)//10
hot_dogBunPkgs_needed = (usr_input*usr_input2) // 8
hotDogLeftOver = (usr_input*usr_input2) % 10
bunLeftOver = (usr_input*usr_input2) % 8

print("The minimum number of hot dog packages needed is " + str('%.f'%hot_dogPkgs_needed))
print("The minimum number of hot dog bun packages needed is " + str('%.f'%hot_dogBunPkgs_needed))
print("There will be " + str('%.f'%hotDogLeftOver) + " hot dogs left over")
print('There will be ' + str('%.f'%bunLeftOver) + ' hot dog buns left over')


    
