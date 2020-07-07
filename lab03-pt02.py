import time
user_input = input("Please enter the weather (i.e. sunny, windy, rainy): ")
possible_weather_choices = ['sunny', 'windy', 'rainy']
user_input2= input("Please enter your destination (i.e beach, school, daycare): ")
possible_destination_choices =['beach', 'school', 'daycare']
if (user_input == possible_weather_choices[0] or user_input == possible_weather_choices[1] or user_input == possible_weather_choices[2]
    and user_input2 == possible_destination_choices[0] or user_input2 ==possible_destination_choices[1] or user_input2 == possible_destination_choices[2]):
    print("The computer will now decide the outfit... Please wait")
    time.sleep(1)
    if ( user_input == possible_weather_choices[0] and user_input2 == possible_destination_choices[0] or user_input2 == possible_destination_choices[1] or
         user_input2 == possible_destination_choices[2]):
        print("Your child should wear something light like shorts because it is sunny and you're child will be out for a bit.")
    elif ( user_input == possible_weather_choices[1] and user_input2 == possible_destination_choices[0] or user_input2 == possible_destination_choices[1] or
           user_input2 == possible_destination_choices[2]):
        print('Your child should wear some mild protection, like a light hoodie because it is windy and could get cold')
    elif ( user_input == possible_weather_choices[2] and user_input2 == possible_destinaation_choices[0] or user_input2 == possible_destination_choices[1] or
           user_input2 == possible_destination_choices[2]):
        print("Your child should wear or carry some protective clothing, like a rain coat. It is rainy and could get worse")
else:
    print("Please enter a valid weather or destination input from the options listed")
    
