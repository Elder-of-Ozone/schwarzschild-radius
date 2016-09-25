
class User():

    username = ""
    
    settings = {}

    user = {}

    planets = {}

    fleets = {}


   # The following functions will edit this field 
    
    def getUsersPlanets(self, user, planets, pid=[]):
        planets_id = [x for x in user["planetID"]]
        plist = []
        for i in planet_id:
            plist.append(planets[i])

        return plist

    def grabPlanetObj(user, fleets, fid=[]):
        fleet_id = [ x for x in user["fleetID"]]
        flist = []
        for i in fleet_id:
            flist.append(fleet[i])


