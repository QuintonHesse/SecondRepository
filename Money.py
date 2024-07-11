Denominations = {'dollar': 100, 'quarter': 25, 'dime': 10, 'nickel': 5, 'penny': 1}
user_input = int(input())
if user_input <= 0:
    print('No change')
num_dollars = user_input // 100
user_input = user_input - num_dollars * 100
print(user_input)
