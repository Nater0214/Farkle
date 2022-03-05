# Imports
from os import system
from random import randint


# Deffinitions
class Dice: # Dice variables and methods
    # Variables
    saved = []
    unsaved = []

    # Methods
    def roll(self, amount = len(unsaved)): # Rolls the dice
        self.unsaved = []
        for i in range(amount):
            self.unsaved.append(randint(1, 6))
    
    def reroll(self): # Same as self.roll but instead resets everything for a new turn
        self.saved = []
        self.roll(6)
    
    def display(self): # Prints all the dice values
        print(f"Saved: {self.saved}\nUnsaved: {self.unsaved}")
dice = Dice()


def get_input(inp):
    if inp == "r":
        dice.roll()
    if inp == "s":
        try:
            inp = int(input())
        except:
            return
        if inp not in range(1, len(dice.unsaved)):
            return
        dice.saved.append(dice.unsaved[inp - 1])
        dice.unsaved.pop(inp - 1)


turns = 0

system("cls")
print("Welcome to Farkle!")

while True: # Game Loop
    dice.reroll()
    while True:
        dice.display()
        inp = input()
        get_input(inp)