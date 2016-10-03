#!/usr/bin/python

from UIView import UIView

class Controller():
    
    def __init__(self, View, User, Time):

        self.View = View
        self.User = User
        self.Time = Time

    def updateView(self):
        ret = self.View.show_menu(self.User, self.Time)
        #self.View.menu(self.User, self.Time)

        if ret == "1":
            self.View.show_user(self.User)
        elif ret == "2":
            self.add_option(self.User, self.User.fleets, self.User.planets)
        elif ret == "3":
            select_planet = self.View.viewPlanets(self.User.planets)
            building_id = self.View.add_structure(select_planet, self.availableStructuresForUser())
            self.structure(select_planet, building_id)

        elif ret == "u":
            self.Time.updateServerCreation()
        elif ret == "n":
            self.evalTurn()
        else:
            return 0

    def add_option(self,user, fleets, planets):

        obj, key, val = self.View.add_option(user, planets, fleets)
        
        if obj == "user":
            user.user[key] = val
        elif obj == "planet":
            #planet_id = input("Enter Planet ID")
            planet_id = "1" # testing purposes
            planets[planet_id][key] = val

        elif obj == "fleet":
            fleet_id = input("Enter Fleet ID")
            fleet_id = "1"
            fleets[fleet_id][key] = val

        user.save_objs()


    def structure(self,planet,building_id):
        
        
        print(planet)
        print(building_id)
        structures = buildingFactory.listOfBuildings()
        planet["1"][structure].increaseQuantity(planet["1"])


        building_id = int(building_id) - 1
        self.User.planets["1"][structures[building_id]] = int(self.User.planets["1"][structures[building_id]]) + 1
        self.User.planets["1"]["metals"] = int(self.User.planets["1"]["metals"]) - cost_in_metals[building_id] 
        self.User.planets["1"]["rareEarthElement"] = int(self.User.planets["1"]["rareEarthElement"]) - cost_in_rareEarth[building_id]  
        # Add to queue
        self.User.save_objs()


    def populationDynamics(self):
        """
        This will evolve to be exponantial eventually
        However until then, it's linear
        P = P0 e^tx where x is exp coefficient
        MaxPop = Housing * 1000
        P = P + 200
        """

        for key, planet in self.User.planets.items():
            planet["population"] = int(planet["population"]) + 200
            if int(planet["population"]) > (int(planet["housing"]) * 1000):
                planet["populaton"] = int(planet["housing"]) * 1000

    def updateResources(self):
        self.populationDynamics()

        for key, planet in self.User.planets.items():
            planet["rareEarthElement"] = int(planet["rareEarthElement"]) + (200 * int(planet["mine"]))
            planet["metals"] = int(planet["metals"]) + (500 * int(planet["mine"]))
            planet["food"] = int(planet["food"]) + (500 * int(planet["farm"]))

    def evalTurn(self):
        self.User.settings["turn"] = int(self.User.settings["turn"]) + 1
        self.updateResources()
        print("eval'd turn")
        self.User.save_objs()

    def updateQueue(self):
        print("updated queue")

    def availableStructuresForUser(self):
        print("To be implemented")
