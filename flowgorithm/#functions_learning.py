#functions_learning


def welcome ():
    print("Helllo, I´m here!")
    
#Call function
welcome()
from random import randint
    
def rollDice():
        die1= randint(1,6)
        die2= randint(1,6)
        print(f"Die 1 : {die1}")
        print(f"Die 2 : {die2}")
        
rollDice()

def rollDice2():
    die1 = randint (1,6)
    die2 = randint (1,6)
    return die1, die2

print (rollDice2())
