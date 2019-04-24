from ShipClassifier import ShipClassifier
from bs4 import BeautifulSoup
import requests
import json

class shipParser(object):

    def parse(self, pointer: int):
        r = requests.get("https://azurlane.koumakan.jp/List_of_Ships")

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        wikitables = soup.findAll("table", "wikitable sortable jquery-tablesorter")

        try:
            with open("shipList.json", "r") as f:
                try:
                    craftableShips = json.load(f) # If updating list
                except ValueError:
                    craftableShips = {"N": [], "R": [], "SR": [] , "SSR": []} # If file exists but nothing in it
            
        except FileNotFoundError:
            craftableShips = {"N": [], "R": [], "SR": [] , "SSR": []} # If file does not exist

        checker = ShipClassifier()

        table = wikitables[0] # The soup returns several tables (Standard, PR, Collab, Retrofit)
        
        rows = table.findAll("tr") # Rows of the table

        for i in range(pointer, len(rows), 1): # Pointer helps remove the looking over of any ships already indexed
            cells = rows[i].findAll("td") # Cells of the row

            shipID = str(cells[0].find(text=True))
            
            if shipID == "001" or shipID == "002": # Gold and purple bulins
                    continue

            shipHref = "/" + str(cells[1].find(text=True))

            if not checker.craftable(shipHref): # Excludes uncraftable ships
                continue
            
            shipRarity = str(cells[2].find(text=True))
            
            shipInfo = [shipID, shipHref, shipRarity]
            
            if shipRarity == "Normal":
                craftableShips["N"].append(shipInfo)
                    
            elif shipRarity == "Rare":
                craftableShips["R"].append(shipInfo)
                    
            elif shipRarity == "Elite":
                craftableShips["SR"].append(shipInfo)
                    
            elif shipRarity == "Super Rare":
                craftableShips["SSR"].append(shipInfo)
                
        pointer = {"pointer": len(rows)}
        
        with open("info.json", "w") as f:
            json.dump(pointer,f, indent=2)
        
        with open("shipList.json", "w") as f:
            json.dump(craftableShips, f, indent=2)