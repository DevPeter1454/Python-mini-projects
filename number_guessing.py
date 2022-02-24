import random

upper_range_value = input('Type a number: ')
if upper_range_value.isdigit():
    upper_range_value = int(upper_range_value)
    
    if upper_range_value <= 0:
        print('Please enter a number larger than 0 next time. ')
else:
    print('Please enter a number next time. ')
    quit()
random_number = random.randint(0,upper_range_value)

guesses = 0

while True:
    guesses +=1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time. ')
        continue
    
    if user_guess == random_number:
        print('You got it. ')
        break
    elif user_guess > random_number:
            print('You were above the number!')
    else:
            print('You were below the number.')
        
print(f'You got it after {guesses} guesses ')        

