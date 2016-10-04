#!/usr/bin/python3.5

import sys
import shutil
import os
import pickle
import collections #OrderedDict
import TimeContainer
from buildings import buildingFactory

class UIView():

    def __init__(self):
        print("view loaded")

    def show_menu(self, User, Time):
        os.system("clear")
        print("\n","*" * 12, "MENU", "*" * 12)
        print("\n Status: OFFLINE")
        print("", User.username)
        print(" Current Time:", Time.getCurrentTime().time()) #getCurrentTime() returns a datetime object hence time()
        print(" Turns Elapsed:", Time.getCurrentTurn())
        print("\n")
        print(" Population:", User.planets["1"]["population"])
        print("\n")
        print(" 1. List Objects")
        print(" 2. Add Objects")
        print(" 3. Construct Structure\n")
        print("*" * 28, "\n")
        return input("Please make a selection: ")
    
    def show_user(self, user):
        os.system("clear")
       
        print("Game Status")
        print(user.settings)

        userSorted = collections.OrderedDict(sorted(user.user.items()))
        print("\nUser Obj")
        for obj in userSorted:
            print(obj, ": " , user.user[obj])
        
        print("\nPlanet Obj")
        print(user.getUserPlanetsFromList(user.user, user.planets),"\n")

        print("\nFleet Obj")
        print(user.getUserFleetsFromList(user.user, user.fleets), "\n")
        pause = input("")

    def viewPlanets(self, planets):
        os.system("clear")
        
        for key,value in planets.items(): 
            print(key,": ", value["name"])

        return input("Planet Identification Number:")

    def add_structure(self, planet, availableStructuresToBuild=None):
        """
        Build structures.
        """
        os.system("clear")
        building = buildingFactory.listOfBuildings()
        print(" Which Structure To Build:")
        for  value in building:
            print(" *", value)
        
        # Well hello again.  
        # For testing purposes, default is 
        ret = input(" Building Name: ")
        
        if ret is "":
            return "farm"
        else:
            return ret
        #
        #return input(" Building Name: ")


    def add_option(self, user, planets, fleets):
        os.system("clear")
        obj  = input("Object to change: ") #user
        key = input("Key to add/change: ")
        val =  input("Key Value: ")
        return obj, key, val

if __name__ == '__main__':

    Menu = UIView()


