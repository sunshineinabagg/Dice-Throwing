from DiceThrowing.dicethrowing import DiceThrowing, edges_amount

if __name__ == '__main__':

    edges = edges_amount()
    dice = DiceThrowing(int(edges))
    
    while True:
        dices = input('\nHow many dices you want to throw? | ')
        while dices.isnumeric() == False:
            print('\nIncorrect answer. Please, choose againю')
            dices = input('How many dices you want to throw? | ')
        dices = int(dices)
        if dices > 0:
            print(dice.throw(dices))
        else:
            print('\nStop time\n')
            break
