from shipParser import shipParser
import json
import random
from random import choices


def main():

    try:
        with open("info.json", "r") as f:
            info = json.load(f)
            pointer = info["pointer"]
            
    except FileNotFoundError:
        with open("info.json", "w") as f: # Fallback for no info.json existing
             pointer = {"pointer": 1}
             json.dump(pointer, f)
             pointer = 1

    updater = shipParser()

    updater.parse(pointer)

    print("Ship List Updated. Pointer is at {0}".format(pointer))
    print("\n")

    rollCounter = 0

    while (1):
        rolls = int(input("How many rolls do you want to take?\nEnter a value of 0 to quit. "))

        if rolls <= 0:
            print("Exiting!")
            break

        results = roll(rolls)
        print(results)
        print("\n")
    

def roll(numRolls: int):
    
    rarities = ["N", "R", "SR", "SSR"]
    weights = [.3, .51, .12, .07]
    
    shipResults = []
    
    rarityResults = choices(rarities, weights, k=numRolls)

    with open("shipList.json", "r") as f:
        
        shipList = json.load(f)
        
        for rarity in rarityResults:
            ship = random.choice(shipList[rarity])
            shipResults.append(ship[1].split("/")[1]) # Names are formatted as href in the file ex : /Nagato
            
    print(rarityResults) # TODO - Change this?
    return shipResults
        

if __name__ == "__main__":
    main()
