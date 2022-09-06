#Sanake Water Gun Game

import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='c':
            return False
    
    elif comp=='p':
        if you=='c':
            return True
        elif you=='s':
            return False

    elif comp=='c':
        if you=='s':
            return True
        elif you=='p':
            return False

print("Welcome to stone, paper, secissor game\n")
print("Computer chooses stone(s), Paper(p), secissor(c)")
rand=random.randint(1,3)
if rand==1:
    comp='s'
elif rand==2:
    comp='p'
else:
    comp='c'

you=input("Enter your choice Stone(s), Paper(p), secissor(c)\n")
a=game(comp,you)
print("Computer choose "+ comp)
print("You Choose "+ you)
if a==None:
    print("Game is tie")
elif a:
    print("You Won :)")
else:
    print("You Lose :(")
