import random

class DiceThrowing:
    def __init__(self, edges):
        self.edges = edges

    def throw(self, amount):
        result = []
        for i in range(amount):
            result.append(random.randint(1, self.edges))
        return result   

dice = DiceThrowing(20)
print(dice.throw(5))
