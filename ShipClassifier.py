import requests
from bs4 import BeautifulSoup


class ShipClassifier(object):


    '''def notePresence(self, shipHref: str):

        r = requests.get("https://azurlane.koumakan.jp" + shipHref)

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        wikitables = soup.findAll("table", "wikitable")

        presence = False

        for table in wikitables:
            rows = table.findAll("tr")

            for i in range(1, len(rows), 1):
                notes = rows[i].findAll("th")
        
                for note in notes:
                               
                    if note.text.strip() == "Additional Notes":
                        print("??")
                        presence = True
                        
        return presence'''

    def craftable(self, shipHref: str):
        
        r = requests.get("https://azurlane.koumakan.jp" + shipHref)

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        wikitables = soup.findAll("table", "wikitable")

        craftable = True

        for table in wikitables:
            rows = table.findAll("tr")

            for i in range(1, len(rows), 1):
                notes = rows[i].findAll("td")
           
                for note in notes:
                               
                    if note.text.strip() == "Cannot Be Constructed":
                        craftable = False
                        
        return craftable

    
