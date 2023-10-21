import beverages
import random


class CoffeeMachine():
    def __init__(self):
        self.broken = False
        self.drinks_served = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.90
            self.name = "empty cup"
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.broken = False
        self.drinks_served = 0

    def serve(self, beverage):
        if self.broken:
            raise self.BrokenMachineException()
        self.drinks_served += 1
        if self.drinks_served > 10:
            self.broken = True
            raise self.BrokenMachineException()
        return random.choice([beverage, self.EmptyCup()])

def machine():
    machine = CoffeeMachine()

    try:
        while True:
            drink = machine.serve(random.choice([beverages.HotBeverage(), beverages.Coffee(), beverages.Tea(), beverages.Chocolate(), beverages.Cappuccino()]))
            print(drink)
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        machine.repair()

if __name__ == '__main__':
    machine()