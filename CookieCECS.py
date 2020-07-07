sugar = float(1.5)
butter = float(1)
flour = float(2.75)
cookies_48 = 48

desired_cookies_input = int(input('How many cookies would you like? '))
desired_cookies_proportion = (desired_cookies_input/cookies_48)
desired_cookies_sugar = (desired_cookies_proportion * sugar)
desired_cookies_butter = (desired_cookies_proportion * butter)
desired_cookies_flour = (desired_cookies_proportion * flour)

print('You will need ' + str('%.2f'%desired_cookies_sugar) + ' cups of sugar, ' + str('%.2f'%desired_cookies_butter) + ' cups of butter, and ' +
      str('%.2f'%desired_cookies_flour) + ' cups of flour.')





                    


