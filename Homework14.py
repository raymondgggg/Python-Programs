#Raymond Guevara
#Homework 14
#018504731

# 8.5 Alphabetic Telephone Number
usr_input = input("Please enter a phone number (XXX-XXX-XXXX): ").upper()
for i in usr_input:
    if not i.isalpha():
        print(i, end = '')
    elif i == 'A' or i == 'B' or i == 'C':
        print('2', end = '')
    elif i == 'D' or i == 'E' or i == 'F':
        print('3', end = '')
    elif i == 'G' or i == 'H' or i == 'I':
        print('4', end = '')
    elif i == 'J' or i == 'K' or i == 'L':
        print('5', end = '')
    elif i == 'M' or i == 'N' or i == 'O':
        print('6', end ='')
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        print('7', end = '')
    elif i == 'T' or i == 'U' or i == 'V':
        print('8', end = '')
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        print('9', end = '')

        
        
