#!/usr/bin/python

from UIView import UIView

class Controller():

    def __init__(self, View, User, Time):

        self.User = User
        self.Time = Time

        if View.__class__.__name__ == "FrontEnd":
            self.FrontEnd = View
        else:
            self.View = View


    # Depreciated
    def updateView(self):
        ret = self.View.show_menu(self.User, self.Time)
        #self.View.menu(self.User, self.Time)

        if ret == "1":
            self.View.show_user(self.User)
        elif ret == "2":
            self.add_option(self.User, self.User.fleets, self.User.planets)
        elif ret == "3":
            select_planet = self.View.view_planets(self.User.planets)
            select_planet = "1"
            building_id = self.View.add_structure(self.User.planets[select_planet], self.availableStructuresForUser())
            self.structure(select_planet, building_id)

        elif ret == "u":
            self.Time.updateServerCreation()
        elif ret == "n":
            self.evalTurn()
        else:
            return 0

    def add_option(self,user, fleets, planets):
        """ This is currently broken.

            If you want to change a variable, please hard coded in the
            add_option() within UIView.py file.absolute_import

        """
        obj, key, val = self.View.add_option(user, planets, fleets)

# Uncomment once fixed

        #if obj == "user":
        #    user.user[key] = val
        #elif obj == "planet":
        #    #planet_id = input("Enter Planet ID")
        #    planet_id = "1" # testing purposes
        #    planets[planet_id].key = val

        #elif obj == "fleet":
        #    fleet_id = input("Enter Fleet ID")
        #    fleet_id = "1"
        #    fleets[fleet_id][key] = val

        user.save_objs()


    def structure(self,planetID,buildingName):

        #structures = buildingFactory.listOfBuildings()

        planetID = "1"
        # Replace "1" with planetID after testing.

        # p and b are just aliases for the following:

        p = self.User.planets[planetID]

        if buildingName == "city":
            b = self.User.planets[planetID].city
        elif buildingName == "mine":
            b = self.User.planets[planetID].mine
        elif buildingName == "farm":
            b = self.User.planets[planetID].farm
        elif buildingName == "housing":
            b = self.User.planets[planetID].housing

        i = 0
        for resource, value in b.construction.items():
            quantity = getattr(p, resource)
            if (quantity - value) > 0:
                print("enough resource of", resource)
                i+=1
        if True :#i == (len(b.outputDict) - 1):
            for resource, value in b.construction.items():
                quantity = getattr(p, resource)
                setattr = (p, resource, (quantity-value))
                b.quantity +=1 
                # Need to add to 
            #p[resource] -= value

        #input()
        
        
        
        #self.User.planets[planetID][buildingName].quantity +=1

        #ret = self.User.planets["1"][buildingName].increaseQuantity() #or .quantity + 1
        #if ret:
        #   return True
        #else:
        #    return False
        #iself.User.planets["1"][structures[building_id]] = int(self.User.planets["1"][structures[building_id]]) + 1
        #self.User.planets["1"]["metals"] = int(self.User.planets["1"]["metals"]) - cost_in_metals[building_id] 
        #self.User.planets["1"]["rareEarthElement"] = int(self.User.planets["1"]["rareEarthElement"]) - cost_in_rareEarth[building_id]  
        #input
        # Add to queue
        self.User.save_objs()


    def populationDynamics(self, idx, planet):
        """
        This will evolve to be exponantial eventually
        However until then, it's linear
        P = P0 e^tx where x is exp coefficient
        MaxPop = Housing * 1000
        P = P + 200
        """
        print(planet.population+50)
        planet.population = planet.populaton + 20
        #if planet.population > (planet.housing.quantity * 200):
        #    planet.populaton = planet.housing.quantity * 200

    def updateResources(self, idx, planet):
        for resource, quantity in planet.resource.items():
            print("resource:", resource, quantity)
            if resource == "metals":
                if resource in planet.mine.outputDict:
                    planet.resource[resource] = quantity +  int(planet.mine.quantity) * planet.mine.outputDict[resource]
            elif resource == "rareEarth":
                if resource in planet.mine.outputDict:
                    planet.resource[resource] = quantity + int(planet.mine.quantity) * planet.mine.outputDict[resource]
            elif resource == "food":
                if resource in planet.farm.outputDict:
                    planet.resource[resource] = quantity + int(planet.farm.quantity) * planet.farm.outputDict[resource]

    def evalTurn(self):
        for key, planet in self.User.planets.items():
            self.populationDynamics(key, planet)
            self.updateResources(key, planet)
            self.updateQueue(key, planet)
        #self.User.settings["turn"] = int(self.User.settings["turn"]) + 1
        #self.User.save_objs()

    def updateQueue(self, idx, planet):
        for queue in planet.queue:
            print(queue[0].name)
            if queue[1] == 1:
                queue[0].increaseQuantity(planet)
                del(planet.queue[0])
            else:
                queue[1] -= 1

        #print(self.User.planets["1"].queue)
        #print("updated queue")

    def availableStructuresForUser(self):
        print("To be implemented")

    def combat(fleet1, fleet2):
        fleets = ["Scout","Outpost","Freighter","Bomber","Fighter","Frigate", "Destroyer", "Battleship", "Dreadnaught"]

        attack_array = [[1,2,8,16,32],
                        [1,1,4,16,32],
                        [0.25,0.125,1,2,8,16]
                        [0.125,0.25,2,1,8,16]
                        [0.0625,0.03125,0.125,0.0625,1,2]
                        [0.03125,0.0625,0.0625,0.125,2,1]]

