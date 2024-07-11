def shampoo_instructions(cycles):
    if user_cycles<1:
        print('Too few')
    elif user_cycles>4:
        print('Too many')
    else:
        Num = 1
        while Num <= user_cycles:
            print(Num, ': Lather and rinse.')
            Num = Num + 1
user_cycles = int(input())
shampoo_instructions(user_cycles)