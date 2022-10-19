from DiceThrowing.dicethrowing import DiceThrowing

if __name__ == '__main__':
    dice = DiceThrowing(20)
    while True:
        a = int(input('How many dices you want to throw? \n'))
        if a > 0:
            print(dice.throw(a))
        else:
            print('Stop time')
            break            