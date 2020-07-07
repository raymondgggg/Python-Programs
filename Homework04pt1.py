import time
houses = [1,2,3,4,5,6,7,8,9,10] #House 3, 6, and 9 have dogs at gate
mailman_house_number = int(input('Please enter house number: '))
if (mailman_house_number == houses[2] or mailman_house_number == houses[5]
    or mailman_house_number == houses[8]):
    print("The mailman throws a bone so he an ring the bell")
    time.sleep(.5)
    while houses[0] <= 3:
        print("The mail man is ringing the bell")
        time.sleep(.5)
        houses[0] += 1
    time.sleep(.5)
    print("The mailman sets down the package")
else:
    time.sleep(.75)
    print("The mailman hands over the package to the person who opens the door")
    
    
