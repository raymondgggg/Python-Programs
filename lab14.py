#Raymond Guevara
#Lab 14
#018504731

#Programming exercises 8.1
print("Problem 8.1")
usr_input = input("Please enter your name: ")
mylist = usr_input.split()
print("Your intials are ", end = '')
for ch in mylist:
    print(ch[0]+ ".",end="")
print()

#Programming exercise 8.3
print("Problem 8.3")
usr_input = input("Please enter a date (mm/dd/yyyy): ")
dateList = usr_input.split('/')
monthName = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November',
             'December']
for i in range(12):
    if i == int(dateList[0]):
        print(monthName[i-1], dateList[1] + ',', dateList[2])
        break
    if 12 == int(dateList[0]):
        print(monthName[11], dateList[1] + ',', dateList[2])
        break
print()

#Programming exercise 8.9
print("Problem 8.9 Vowel and Consonant")
vowel = 'aeiou'
vowel_ct = 0
consonant_ct = 0

sentence = input("enter a sentence: " ).lower()
for ch in sentence:
    if ch in vowel:
        vowel_ct += 1
    elif ch >='b' and ch <= 'z':
        consonant_ct += 1
print("There are " + str(vowel_ct), "vowels")
print("There are " + str(consonant_ct), "Consonant")




        
    
    
    



    
