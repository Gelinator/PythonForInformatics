#To ask the player what number he/she chooses

import random
print "Welcome to my dice throwing game!"


while True:
    try:
        choice = int(raw_input("Please enter your choice, a number from one to 6:\n"))
        if choice <= 6 and choice >= 1:
            break
    except:
        choice = int(raw_input("Please enter a valid number from one to 6:\n"))
        if choice <= 6 and choice >= 1:
            break
throw = random.randint(1,6)
print ("The dice returns a %s!" %(throw))

if throw == choice:
    print "Good job! You just won NOTHING!"
    
else:
    print "You lose"
