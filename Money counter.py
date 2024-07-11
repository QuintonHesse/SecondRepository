Denominations = {'Dollars': 100, 'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
user_input = int(input('Enter  amount '))
if user_input <= 0:
    print('No change')
num_dollars = user_input // 100
user_input = user_input - num_dollars * 100
num_quarters = user_input // 25
user_input = user_input - num_quarters * 25
num_dimes = user_input // 10
user_input = user_input - num_dimes * 10
num_nickels = user_input // 5
user_input = user_input - num_nickels * 5
num_pennies = user_input // 1
user_input = user_input - num_pennies * 1
if num_dollars == 1:
    print(num_dollars, 'Dollar')
elif num_dollars > 1:
    print(num_dollars, 'Dollars')
if num_quarters == 1:
    print(num_quarters, 'Quarter')
elif num_quarters > 1:
    print(num_quarters, 'Quarters')
if num_dimes == 1:
    print(num_dimes, 'Dime')
elif num_dimes > 1:
    print(num_dimes, 'Dimes')
if num_nickels == 1:
    print(num_nickels, 'Nickel')
elif num_nickels > 1:
    print(num_nickels, 'Nickels')
if num_pennies == 1:
    print (num_pennies, 'Penny')
elif num_pennies > 1:
   print(num_pennies, 'Pennies')
