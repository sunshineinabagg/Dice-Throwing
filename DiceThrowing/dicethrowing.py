import random

class DiceThrowing:
    def __init__(self, edges):
        self.edges = edges

    def throw(self, amount):
        result = []
        for i in range(amount):
            result.append(random.randint(1, self.edges))
        return result
    
def edges_amount():
    edges = input('How many edges on your dices? Choose 6, 8 or 20. | ')
    while edges not in ('6', '8', '20'):
        print('\nIncorrect answer. Please, choose again')
        edges = input('How many edges on your dices? Choose 6, 8 or 20. | ')
    return edges