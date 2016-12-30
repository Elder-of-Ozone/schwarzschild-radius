import pickle
from buildings import buildingFactory
from planet import planet

class User():

    username = "hydrius"
    
    settings = {
            "turn": "1",
            "created": "Days and days ago",
                   }

    user = {
            "username": "Hydrius",
            "economy" : 9000,
            "planet_ID": ["1"],
            "fleet_ID": ["1"],
            }

    planets = {
            "1" : planet("Nopeming")
            
            }

    fleets = {
                "1": {
                    "ships": 100, 
                },
            }


    def __init__(self):
        self.load_objs()

   # The following functions will edit this field 
   
    def load_objs(self):
        try:
            with open('settings.objs','rb') as file: 
                self.settings = pickle.load(file)
        except:
            print("Unable to load, reverting to default")

        try:
            with open('user.objs','rb') as file:
                self.user = pickle.load(file)
        except:
             print("Unable to load, reverting to default")

        try: 
            with open('planets.objs','rb') as file:
                self.planets = pickle.load(file)
        except:
            print("Unable to load, reverting to default")

        try:
            with open('fleet.objs','rb') as file:
                self.fleets = pickle.load(file)
        except:
            print("Unable to load, reverting to default")

    def save_objs(self):
        with open('settings.objs', 'wb') as handles:
            pickle.dump(self.settings,handles)

        with open('user.objs', 'wb') as handles:
                pickle.dump(self.user, handles)
        with open('fleet.objs', 'wb') as handles:
            pickle.dump(self.fleets, handles)
        with open('planets.objs', 'wb') as handles:
            pickle.dump(self.planets, handles)
        print("saved")

    def getUserPlanetsFromList(self, user, planets, pid=[]):
        planet_id = [x for x in user["planet_ID"]]
        plist = []
        for i in planet_id:
            plist.append(planets[i])

        return plist

    def getUserFleetsFromList(self,user, fleets, fid=[]):
        fleet_id = [ x for x in user["fleet_ID"]]
        flist = []
        for i in fleet_id:
            flist.append(fleets[i])

        return flist


