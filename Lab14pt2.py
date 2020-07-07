#Raymond Guevara
#Lab 14 part 2
#01804731

# 8.2 sum of digits in a String
print("Sum of digits in a String")
usr_input = input("Please enter a series of numbers: ")
count = 0
for i in usr_input:
    count += int(i)
print(count)
print()

#8.11 word separator 
print("8.11 Word separator")
usr_input = input("Enter a sentence: ")
print(usr_input[0], end = '')
for i in usr_input[1:]:
    if i.isupper():
        print(' ', end = '') 
        print(i.lower(), end = '')
    if i.islower():
        print(i, end = '')
            
    
        

    
