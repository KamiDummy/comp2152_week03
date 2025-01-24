import random
# dice options
diceOptions  = list(range(1, 7))

#Wepons array 
weapons = ["fist", "knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Diplsay available weapons 
print ("Available weapons: ", ', '.join(weapons))

def  get_combat_strength(prompt) :
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else: 
                print ("value invalid, me wants 1-6")
        except ValueError:
            print("Invalid input")

combatStrength = get_combat_strength("Enter your combat strength (1-6)")
monsterStrength = get_combat_strength("Enter monster combat strength (1-6)")

for j in range(1, 21, 2):
