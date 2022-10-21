from DiceThrowing.dicethrowing import DiceThrowing, edges_amount

if __name__ == '__main__':

    edges = edges_amount()
    dice = DiceThrowing(int(edges))
    
    while True:
        dices = int(input('\nHow many dices you want to throw? | '))
        if dices > 0:
            print(dice.throw(dices))
        else:
            print('\nStop time\n')
            break            