import time 
side_a = int(input("Please enter side a: "))
side_b = int(input("Please enter side b: "))
side_c = int(input("Please enter side c: "))
if (side_a == side_b and side_a == side_c):
    print("The side lengths indicate this is an equilateral triangle")
elif (side_a == side_b or side_a == side_c or side_b == side_c):
    print("The side lengths indicate this is an isosceles triangle")
else:
    print("Based off the side lengths, the triangle is neither an isosceles or equilateral triangle")
time.sleep(2)

    
