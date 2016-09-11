#!/usr/bin/python3.5

import sys
import shutil
import os
import pickle
import collections #OrderedDict

user = {"economy": 9001, # It's over 9000!
        "planetNum": 1,
        "planetID": ["1"],
       "fleetNum": 1,
        "fleetID": ["1"],
        }

# Fleet Table
# ID Name Ships
#fleets = {"1" : {"ships": 100000},
#         } 

# planet table
# ID City Education

planets = {"1" : {"city": 1,       # city ->  capital -> Metropolies 
                "education": 1},  # University Levels}
        }


def grabPlanetObj(user, planets, pid=[]):
    """ 
    Grab planets from user id
    """

    planet_id = [x for x in user["planetID"]] 
    plist = []
    for i in planet_id:
        plist.append(planets[i])
    
    return plist

def grabFleetObj(user, fleet, pid=[]):
    """
    Grab fleet from user id
    """

    fleet_id = [ x for x in user["fleetID"]]
    flist = []
    for i in fleet_id:
        flist.append(fleet[i])

    return flist


def show_user(user):
    os.system("clear")
    
    userSorted = collections.OrderedDict(sorted(user.items()))
    for obj in userSorted:
        print(obj, ": " , user[obj])

    print("\n Planet Obj")
    print(grabPlanetObj(user, planets),"\n")
    pause = input("")
    print("\n Fleet Obj")
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
        planets[pid][name] = ret 
    elif obj == "fleets":
        pid = input("enter fleet ID: ")
        fleets[pid][name] = ret 
    
    save_objs()

def save_objs():

    with open('user.objs', 'wb') as handles:
        pickle.dump(user, handles)
        print("Saved user objects")

    with open('fleet.objs', 'wb') as handles:
        pickle.dump(fleets, handles)
        print("Saved fleet objects")
        
    with open('planet.objs', 'wb') as handles:
        pickle.dump(planets, handles)
        print("Saved planet objects")
    ret = input("Saved")
def load_objs():
    try:
        with open('user.objs', 'rb') as handles:
            user = pickle.load(handles)
            print("Loaded user objects")
    except:
        user = {"economy": 9001, # It's over 9000!
                "planetNum": 1,
                "planetID": ["1"],
                "fleetNum": 1,
                "fleetID": ["1"],
            }
    with open('fleet.objs', 'rb') as handles:
        fleets = pickle.load(handles)
        print("Loaded fleet objects")
    #except:
       # fleets = {"1" : {"ships": 100000},
        #    } 


    try:
        with open('planet.objs', 'rb') as handles:
            planet = pickle.load(handles)
            print("Saved planet objects")
    except:
        planets = {"1" : {"city": 1,       # city ->  capital -> Metropolies 
                   "education": 1},  # University Levels}
                }

def show_menu():
    os.system("clear")
    print("\n","*" * 12, "MENU", "*" * 12)
    print("1. List objects")
    print("2. Add objects")
    print("3. Delete objects")
    print("*" * 28, "\n")
    return input("Please make a selection: ")

load_objs()

while True:
    ret = show_menu()
    if ret  == "1":
        show_user(user)
    elif ret == "2":
        add_option()
    else:
        print("No Values")
        break
