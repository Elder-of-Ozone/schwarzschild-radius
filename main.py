#!/usr/bin/python3.5

import sys
import shutil
import os
import pickle
import collections #OrderedDict
import TimeContainer


user = {}
fleets = {}
planets = {}

def grabPlanetObj(user, planets, pid=[]):
    """ 
    Grab planets from user id
    """

    planet_id = [x for x in user["planetID"]] 
    plist = []
    for i in planet_id:
        plist.append(planets[i])
    
    return plist

def grabFleetObj(user, fleets, pid=[]):
    """
    Grab fleet from user id
    """

    fleet_id = [ x for x in user["fleetID"]]
    flist = []
    for i in fleet_id:
        flist.append(fleets[i])

    return flist


def show_user(user):
    os.system("clear")
    
    userSorted = collections.OrderedDict(sorted(user.items()))
    print("User Obj")
    for obj in userSorted:
        print(obj, ": " , user[obj])

    print("\nPlanet Obj")
    print(grabPlanetObj(user, planets),"\n")
    print("\nFleet Obj")
    print(grabFleetObj(user, fleets), "\n")
    pause = input("")


def add_option():
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
    
    save_objs()

def save_objs():

    with open('user.objs', 'wb') as handles:
        pickle.dump(user, handles)

    with open('fleet.objs', 'wb') as handles:
        pickle.dump(fleets, handles)
        
    with open('planet.objs', 'wb') as handles:
        pickle.dump(planets, handles)
    ret = input("Saved")

def load_objs():
    try:
        with open('user.objs', 'rb') as handles:
            global user
            user = pickle.load(handles)
    except:
        user = {"economy": 9001, # It's over 9000!
            "planetNum": 1,
            "planetID": ["1"],
            "fleetNum": 1,
            "fleetID": ["1"],
            }
    try:
        with open('fleet.objs', 'rb') as handles:
            global fleets
            fleets = pickle.load(handles)
    except:
        fleets = {"1" : {"ships": 100000},
            } 

    try:
        with open('planet.objs', 'rb') as handles:
            global planets
            planets = pickle.load(handles)
    except:
        planets = {"1" : {"city": 1,       # city ->  capital -> Metropolies 
                   "education": 1},  # University Levels}
                  }

    ret = input("Loaded Documents")

def show_menu():
    os.system("clear")
    print("\n","*" * 12, "MENU", "*" * 12)
    print("1. List objects")
    print("2. Add objects")
    print("3. Delete objects")
    print("*" * 28, "\n")
    return input("Please make a selection: ")

load_objs()
try:
    TimeContainer1 = TimeContainer.TimeContainer(user["turn"])
except:
    TimeContainer1 = TimeContainer.TimeContainer() 
while True:
    ret = show_menu()
    if ret  == "1":
        show_user(user)
    elif ret == "2":
        add_option()
    else:
        save_objs()
        break
