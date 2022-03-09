# Imports
from os import system
from random import randint


# Deffinitions
class Dice: # Dice variables and methods
    # Variables
    saved = []
    unsaved = []


    # Methods
    def roll(self, amount): # Rolls the dice
        self.unsaved = []
        for i in range(amount):
            self.unsaved.append(randint(1, 6))


    def reroll(self): # Same as self.roll but instead resets everything for a new turn
        self.saved = []
        self.roll(6)


    def save(self, die):
        self.saved.append(self.unsaved[die - 1])
        self.unsaved.pop(die - 1)

    potential_score = lambda self: None
    unsaved_len = lambda self: len(self.unsaved)

dice = Dice()


def get_input(inp):
    if inp == "r":
        dice.roll(dice.unsaved_len())
    
    elif inp == "s":
        try:
            inp = int(input())
        except:
            return
        if inp not in range(1, dice.unsaved_len()):
            return
        dice.save(inp)
    
    elif inp == "b":
        return "b"
    


clear = lambda: system("cls")
display = lambda: print(f"Turn: {turns}\nScore: {score}\nSaved: {dice.saved}\nUnsaved: {dice.unsaved}\nPotential Score: {dice.potential_score()}")

turns = 1
score = None

clear()
print("Welcome to Farkle!")

while True: # Game Loop
    dice.reroll()
    while True:
        display()
        inp = input()

        if get_input(inp) == "b":
            break
    
    turns += 1