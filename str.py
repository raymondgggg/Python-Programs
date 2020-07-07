while True:
    number = input("enter a number")

    if number.isdigit():
        print(number+"+2=", int(number)+2)
    else:
        print("You did not enter a number")
        continue
    again = input("Do you want to play again? (y/n)")
    if again == 'n':
        break

from random import randint
for i in range(10):
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(d1,d2)

vowel = 'aeiou'
vowel_ct = 0
consonant_ct = 0

sentence = input("enter a sentence: " ).lower()
for ch in sentence:
    if ch in vowel:
        vowel_ct += 1
    elif ch >='b' and ch <= 'z':
        consonant_ct += 1
print(vowel_ct)
print(consonant_ct)


        
