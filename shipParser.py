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
                    craftableShips = json.load(f)
                except ValueError:
                    craftableShips = {"N": [], "R": [], "SR": [] , "SSR": []}
            
        except FileNotFoundError:
            craftableShips = {"N": [], "R": [], "SR": [] , "SSR": []}


        checker = ShipClassifier()

        table = wikitables[0]
        
        rows = table.findAll("tr")

        for i in range(pointer, len(rows), 1):
            cells = rows[i].findAll("td")

            shipID = str(cells[0].find(text=True))
            
            if (shipID == "001" or shipID == "002"):
                    continue

            shipHref = "/" + str(cells[1].find(text=True))

            if (not checker.craftable(shipHref)):
                continue
            
            shipRarity = str(cells[2].find(text=True))
            
            shipInfo = [shipID, shipHref, shipRarity]
            
            if (shipRarity == "Normal"):
                craftableShips["N"].append(shipInfo)
                    
            elif (shipRarity == "Rare"):
                craftableShips["R"].append(shipInfo)
                    
            elif (shipRarity == "Elite"):
                craftableShips["SR"].append(shipInfo)
                    
            elif (shipRarity == "Super Rare"):
                craftableShips["SSR"].append(shipInfo)
                
        pointer = {"pointer": len(rows)}
        
        with open("info.json", "w") as f:
            json.dump(pointer,f, indent=2)
        
        with open("shipList.json", "w") as f:
            json.dump(craftableShips, f, indent=2)
                    
    
