# ask name and age in prompts.
name = input('What is your name?')
age = int(input('How old are you?'))
from datetime import date #learned this from the instant feedback tool
current_yr = date.today().year
born = int((current_yr - age))# determine year born in
born_str = str(born) # convert to string for pesky period
print('Hello', name+'!', 'You were born in', born_str + '.')