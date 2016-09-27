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
            self.Time.addArtificalTurn()
        else:
            return 0

    def add_option(self,user, fleets, planets):

        obj, key, val = self.View.add_option(user, planets, fleets)
        
        if obj == "user":
            user.user[key] = val
        elif obj == "planet":
            planet_id = input("Enter Planet ID")
            planet_id = "1" # testing purposes
            planets[planet_id][key] = val

        elif obj == "fleet":
            fleet_id = input("Enter Fleet ID")
            fleet_id = "1"
            fleets[fleet_id][key] = val

        user.save_objs()


    def structure(self,building_id):
        structures = ["mine", "farm", "shipyard", "housing"]
        building_id = float(building_id) - 1
        self.User.user["building"][structures[building_id]]+=1 

    def evalTurn(self):
        user = self.User.user
        for planet in User.getUserPlanetsFromList():
            planet["population"] += planet["housing"] * 50

        
        print("eval'd turn")


    def updateQueue(self):
        print("updated queue")

    def availableStructuresForUser(self):
        print("To be implemented")
