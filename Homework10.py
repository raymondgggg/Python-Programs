#Homework 10
#Raymond Guevara
#018504731
print("3.14 Body Mass Index")
weight = int(input("Please enter your weight: "))
height = int(input("Please enter your height: "))
bmi = (weight * 703)/(height**2)
print("Your BMI is " + str('%.2f'%bmi))
if (bmi >= 18.5 and bmi <= 25):
    print("Your have am optimal weight: ")
elif (bmi < 18.5):
    print("You are underweight")
else:
    print("You are overweight")
    
