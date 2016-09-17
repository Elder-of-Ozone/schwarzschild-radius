#!/usr/bin/python3.5

import sys
import shutil
import os
import pickle
import collections #OrderedDict
import TimeContainer

class DataManagement():


    #Default game settings
    gameObj = { 
            "turn": "",
            "created":"",
        }

    userObj = {
            "economy": 9001, # It's over 9000!
            "planetNum": 1,
            "planetID": ["1"],
            "fleetNum": 1,
            "fleetID": ["1"],
        }
 

    planetsObj = { 
            "1" :   {
                        "city": 1,       # city ->  capital -> Metropolies 
                        "education": 1
                    },  # University Levels}
        
        }

    fleetObj = {
            "1" : { 
                    "ships": 100
                    }
            }



    @staticmethod
    def grabPlanetObj(user, planets, pid=[]):
        """
        Grab planets from user id
        """

        planet_id = [x for x in user["planetID"]] 
        plist = []
        for i in planet_id:
            plist.append(planets[i])
        
        return plist

    @staticmethod
    def grabFleetObj(user, fleets, pid=[]):
        """
        Grab fleet from user id
        """

        fleet_id = [ x for x in user["fleetID"]]
        flist = []
        for i in fleet_id:
            flist.append(fleets[i])

        return flist

    @staticmethod
    def save_objs():

        with open('game.objs', 'wb') as handles:
            pickle.dump(game, handles)

        with open('user.objs', 'wb') as handles:
            pickle.dump(user, handles)

        with open('fleet.objs', 'wb') as handles:
            pickle.dump(fleets, handles)
            
        with open('planet.objs', 'wb') as handles:
            pickle.dump(planets, handles)

    @staticmethod
    def load_objs():
        try:
            with open('game.objs','rb') as handles:
                global game
                game = pickle.load(handles)
        except:
            game = DataManagement.gameObj

        try:
            with open('user.objs', 'rb') as handles:
                global user
                user = pickle.load(handles)
        except:
                user = DataManagement.userObj
        try:
            with open('fleet.objs', 'rb') as handles:
                global fleets
                fleets = pickle.load(handles)
        except:
            fleets = DataManagement.fleetObj
        try:
            with open('planet.objs', 'rb') as handles:
                global planets
                planets = pickle.load(handles)
        except:
            planets = DataManagement.planetsObj
        
        
        ret = input("Loaded Documents")

class MenuViewController(DataManagement):

    def __init__(self):
        self.load_objs()
        self.TimeContainer = TimeContainer.TimeContainer(user["turn"])

        self.getMenuInput()
        

    def getMenuInput(self):
        while True:
            ret = self.show_menu()
            if ret  == "1":
                self.show_user(user)
            elif ret == "2":
                self.add_option()
            elif ret == "u":
                self.TimeContainer.updateServerCreation()
            elif ret == "n":
                self.TimeContainer.increaseTurn()

            else:
                self.save_objs()
                break       


    def show_menu(self):
        os.system("clear")
        print("\n","*" * 12, "MENU", "*" * 12)
        print("\n Status: OFFLINE")
        print(" Current Time:", self.TimeContainer.getCurrentTime().time()) #getCurrentTime() returns a datetime object hence time()
        print(" Turns Elapsed:", self.TimeContainer.getCurrentTurn())
        print("\n")

        print(" 1. List objects")
        print(" 2. Add objects")
        print(" 3. Delete objects")
        print("*" * 28, "\n")
        return input("Please make a selection: ")
    
    def show_user(self,user):
        os.system("clear")
       
        print("Game Status")
        print(game)

        userSorted = collections.OrderedDict(sorted(user.items()))
        print("\nUser Obj")
        for obj in userSorted:
            print(obj, ": " , user[obj])

        print("\nPlanet Obj")
        print(self.grabPlanetObj(user, planets),"\n")
        print("\nFleet Obj")
        print(self.grabFleetObj(user, fleets), "\n")
        pause = input("")


    def add_option(self):
        os.system("clear")
        obj  = input("Object to change: ") #user
        name = input("Key to add/change: ")
        ret =  input("Key Value: ")

        if obj == "user":
            user[name] = ret
        elif obj == "planets":
            pid = input("Enter planet ID")
            pid = "1"
            planets[pid][name] = ret 
        elif obj == "fleets":
            pid = input("enter fleet ID: ")
            pid = "1"
            fleets[pid][name] = ret 
        
        self.save_objs()

if __name__ == '__main__':

    Menu = MenuViewController()


