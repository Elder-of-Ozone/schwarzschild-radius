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
            self.View.add_option(self.User, self.User.fleets, self.User.planets)
        elif ret == "3":
            select_planet = self.View.viewPlanets(self.User.getUserPlanetsFromList(self.User.user, self.User.planets))
            building_id = self.View.add_structure(select_planet, self.availableStructuresForUser())
            self.structure(select_planet, building_id)

        elif ret == "u":
            self.Time.updateServerCreation()
        elif ret == "n":
            self.Time.addArtificalTurn()
        else:
            return 0

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
