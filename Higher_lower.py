import random
print('Welcome to the higher/lower game, Bella!')
lowb = int(input('Enter lower bound:'))
highb = int(input('Enter higher bound:'))
if lowb > highb:
    print('The lower bound must be less than the upper bound.')
    lowb = int(input('Enter lower bound:'))
    highb = int(input('Enter higher bound:'))
hidden_num = random.randint(lowb, highb)
guesses = 0
user_input = int(input('Geuss the number!'))
while user_input != hidden_num:
    if user_input == hidden_num:
        print('You win!')
    elif user_input > hidden_num:
        print('Nope, too high.')
    elif user_input < hidden_num:
        print('Nope, too low')
    guesses += 1
    print(guesses)
    user_input = int(input('Guess again',))
else:
    print('You got it! the number was:', hidden_num)





