import random
import time 
possible_choices = ['rock', 'paper', 'scissors']
user_input = str(input('please pick from ' + possible_choices[0] + ', ' + possible_choices[1]+ ', or ' + possible_choices[2]+ ': '))
if (user_input == possible_choices[0] or user_input == possible_choices[1] or user_input == possible_choices[2]):
    random_computer_choice = random.choice(possible_choices)
    time.sleep(.5) # I used the time function just so the program doesn't run so fast
    print('The computer picks ' + random_computer_choice)
    if (random_computer_choice == user_input):
        print('It is a draw.')
    elif (random_computer_choice == possible_choices[0] and user_input == possible_choices[2]
          or random_computer_choice == possible_choices[1] and user_input == possible_choices[0]
          or random_computer_choice == possible_choices[2] and user_input == possible_choices[1]): 
        print('The Computer wins.')
    elif (random_computer_choice == possible_choices[0] and user_input == possible_choices[1]
          or random_computer_choice == possible_choices[1] and user_input == possible_choices[2]
          or random_computer_choice == possible_choices[2] and user_input == possible_choices[0] ): 
        print('You win.')
    input('Press enter to close program')
else:
    print('Please enter either "rock", "paper", or "scissors"')  

    
