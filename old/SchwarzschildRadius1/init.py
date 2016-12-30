import curses
from AboveTheClouds import Mechanics
import pickle
from TimeMechanics import TimeMechanics
import copy
from buildings import buildings
import sys
from fleet import fleets

# TO DO
#
# 1. Get length of screen.
#



def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def mainMenu():
    screen.addstr(9,2, "Please enter a number:")
    screen.addstr(10,2, "1. View Planet.")
    screen.addstr(11,2, "2. View Fleet.")
    screen.addstr(12,2, "3. View Surrounding Planets.")
    screen.addstr(13,2, "4. Enter Orders (console)")
    screen.addstr(17,2, "8. About")
    screen.addstr(18,2, "9. Exit")

def viewSurroundingPlanets():
    screen.clear()
    screen.border(0)
    screen.addstr(10,5, "Surrounding Planets")
    screen.refresh()
    screen.getch()

# TODO
def planetVisible():
    return False


def viewPlanetChoice(planet):

    x = screen.getch()

    if x == ord("+"):
        playerList = [user, easy]
        global time
        time = TimeMechanics.updateEVERYTHING(playerList, planets, time)
        
    elif x == ord("m"):
        if buildings.builds("mine", user, planet) == False:
            screen.addstr(23, 17, "Not enough resources")
        
    elif x == ord("f"):
        if buildings.builds("farm", user, planet) == False:
            screen.addstr(23, 17, "Not enough resources")
        
    elif x == ord("d"):
        if buildings.builds("desalination", user, planet) == False:
            screen.addstr(23,17, "Not enough resources")
        
        

    elif x == ord("q"): 
        menu()

    elif x == ord("1"):
        user['viewPlanetIndex'] = 0
    elif x == ord("2"):
        user['viewPlanetIndex'] = 1


    

def viewPlanet():
        
        screen.clear()
        screen.border(0)
    

        userPlanet = user['planets'][user['viewPlanetIndex']]
        
        turns = user['turns']

        name = userPlanet['name']
        population = userPlanet['population']
        water = userPlanet['water']
        REE = userPlanet['REE']
        debris = userPlanet['resource']['debris']
        waterResource = userPlanet['resource']['waterResource']
        foodResource = userPlanet['resource']['foodResource']
        REEResource = userPlanet['resource']['REEResource']

        mine = userPlanet['building']['mine']
        farm = userPlanet['building']['farm']
        desalination = userPlanet['building']['desalination']
        


        ######################
        #                    #
        #   Left Hand Side   #
        #                    #
        ######################


        screen.addstr(2,2, "Planet list.") 

        for i, planetName in enumerate(user['planets']):
            screen.addstr(4+i,2,"%d. %s" %(i+1, planetName["name"]))
        


        for i in xrange(1,27):
            screen.addstr(i,15, "#")

           #population = "200"

        screen.addstr(2, 20, "Planet Information")
        screen.addstr(4, 20, "Name:                 %s" % name)



        screen.addstr(6, 20, "Population:           %d" % population)
        screen.addstr(7, 20, "Water Resources:      %d" % waterResource)
        screen.addstr(8, 20, "Food Resources:       %d" % foodResource)
        screen.addstr(9, 20, "Rare Earth's:         %d" % REEResource)
        screen.addstr(10,20, "Debris:               %d" % debris)




        for i in xrange(1,27):
            screen.addstr(i,51, "#")


        screen.addstr(2, 55, "Game information")
        screen.addstr(4, 55, "Time                 %d " % time)
        screen.addstr(5, 55, "Turns                %d " % turns)
        screen.addstr(6, 55, "Visible?             %r" % planetVisible())


        screen.addstr(8, 55, "Misc")
        screen.addstr(10, 55, "Water:                %d" % water)
        screen.addstr(11, 55,"REE:                  %d" % REE)




        screen.addstr(15, 17, "   Buildings            ")
        screen.addstr(17, 17, "M. Mine:                %d" % mine)
        screen.addstr(18, 17, "F. Farm:                %d" % farm)
        screen.addstr(19, 17, "D. Desalination:        %d" % desalination)

        # Fleets section








        screen.addstr(15, 55, "Fleet Information")
        
        screen.refresh()

        viewPlanetChoice(userPlanet)
        viewPlanet()

def menu():
    x = 0
    while x != ord('9'):


        #ASCII Name came from 
        #http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Slant&t=To%20The%20Moon
        name1 = "   ______          ______ __             __  ___   "
        name2 = "  /_  __/____     /_  __// /_   ___     /  |/  /____   ____   ____ "
        name3 = "   / /  / __ \     / /  / __ \ / _ \   / /|_/ // __ \ / __ \ / __ \ "
        name4 = "  / /  / /_/ /    / /  / / / //  __/  / /  / // /_/ // /_/ // / / /"
        name5 = " /_/   \____/    /_/  /_/ /_/ \___/  /_/  /_/ \____/ \____//_/ /_/ "
                                                                                    



        message = "Welcome Captain! We await your orders!"


        #Mechanics = Mechanics.start()
        #Mechanics.start()
        #if not Mechanics.start()
        screen.clear()
        screen.border(0)
        screen.addstr(1,5, name1)
        screen.addstr(2,5, name2)
        screen.addstr(3,5, name3)
        screen.addstr(4,5, name4)
        screen.addstr(5,5, name5)

        screen.addstr(7,2, message)
        mainMenu()
        screen.refresh()
        x = screen.getch()
    
        if x == ord('1'):
            viewPlanet()
    
        if x == ord('2'):
            viewFleet()
   
        if x == ord('3'):
            viewSurroundingPlanets()

        if x == ord('4'):
            order = get_param("Enter orders")

        if x == ord('8'):
            about()

        if x == ord('+'):
            #player list should be in a class + function somewhere.
            playerList = [user, easy]
            time = TimeMechanics.updateEVERYTHING(playerList, planets, time)

        if x == ord('q'):
            sys.exit()
            break
            curses.endwin()
            sys.exit()

        screen.refresh()

    curses.endwin()



def viewFleet():

    
    #   OUTGOINGS
    #
    #   Fleet Name      Origin        Destination         Time
    #   
    #   fleet1
    #   fleet2
    #   fleet3
    #
    #
    #   INCOMING
    #   
    #   Fleet Name      Origin        Destination         Time
    #
    #   fleet1
    #   fleet2
    #   fleet3



    screen.clear()
    screen.border(0)
    screen.addstr(4,5, "OUTGOING")

    screen.addstr(6,5, "Fleet Name")
    screen.addstr(6, 20, "Origin")
    screen.addstr(6, 35, "Destination")
    screen.addstr(6,55, "Time")
    screen.addstr(6,65, "Departed")

    for i, fleetname in enumerate(user["fleets"]):

        screen.addstr(8+i,5, "%d: %s" % (i +1, fleetname["name"]))
        screen.addstr(8+i,20, "%s" % fleetname["origin"])
        screen.addstr(8+i,35, "%s" % fleetname["destination"])
        screen.addstr(8+i,55, "%d" % fleetname["time"])
        screen.addstr(8+i,65, "%r" % fleetname["departed"])

    #box1 = curses.newwin(20, 20, 5, 5)
    #box1.box()    
        
    #screen.refresh()
    #box1.refresh()
    screen.addstr(18, 5, "INCOMING")    
    screen.addstr(20,5, "Fleet Name")
    screen.addstr(20, 20, "Origin")
    screen.addstr(20, 35, "Destination")
    screen.addstr(20,55, "Time")
    screen.addstr(20,65, "Departed")

   
    
    

    screen.refresh()
    
    fleetChoices()
    viewFleet()


def fleetBox():
    box1 = curses.newwin(20,30,5,25)
    box1.box()

    box1.addstr(2,11, "Options")
    box1.addstr(5,11, "1. View")
    box1.addstr(6,11, "2. Move")
    box1.addstr(7,11, "3. Attack")
    box1.addstr(8,11, "4. Pickup")
    box1.addstr(9,11, "5. Drop")

    box1.refresh()
    fleetBoxChoices(box1)
    fleetBox()
def fleetBoxChoices(box1):
    x = screen.getch()

    if x == ord("1"):
        box1.addstr(1,1,"moving")
        box1.refresh()
        screen.getch()
    if x ==ord("q"):
        viewFleet()


def fleetChoices():
   
    x = screen.getch()

    if x == ord("1"):
        fleetBox()

    if x == ord("2"):
        fleetBox()


    if x ==ord("q"):
        menu()




def about():
    screen.clear()
    screen.border(0)
    screen.addstr(3,2, "Write an about message regarding development")
    screen.refresh()
    screen.getch()










if __name__ == "__main__":
    
    # Need to put time in a global dict
    time = 0

    user    = {
                "name"          : "Hydrius",
                "planets"       : None,
                "fleets"        : None,
               "turns"         : 100,
                "viewPlanetIndex": 0
            } 
    easy    = {
                "name"          : "easy",
                "planets"       : None,
                "turns"         : 100, 
            }
    medium  = {}
    hard    = {}

    fleets = {
                "fleet1": {
                            "name": "fleet1",
                            "origin": "p1",
                            "destination": "p2",
                            "time":     10,
                            "departed": False,
                            "fleet": {
                                "fighters": 20,
                                }
                            },
                "fleet2": {
                            "name": "fleet2",
                            "origin": "p2",
                            "destination": "p1",
                            "time":     10,
                            "departed": False,
                            "fleet": {
                                "fighters": 20,
                                }
                            }
            }
            

    planets = {
                "p1": 
                {
                    "name": "p1",
                    "owner": "hydrius",
                    "population": 100,
                    "REE"       : 3,
                    "water"     : 3,

                    "resource": {
                            "debris"    : 100,
                            "waterResource": 500,
                            "foodResource": 500,
                            "REEResource"       : 200,
                    },
                    "building": {
                            "mine": 1,
                            "farm": 1,
                            "desalination": 1,

                        },


                    "fleetOwner": [
                        {
                         "name": "hydrius",
                         "fighters": 100,
                         "bombers" : 100,
                         "cargo"   : 1
                        }]
                 },
                
                 "p2": 
                    {
                    "name" :"p2",
                    "owner": "hydrius",
                    "REE"       : 3,
                    "water"     : 3,
                    "debris"    : 100,
                    "resource": {
                        "debris"    : 100,
                        "waterResource": 500,
                        "foodResource": 500,
                        "REEResource"       : 200,
                    },

                    "building" : {
                        "mine":         2,
                        "farm":         3,
                        "desalination": 2
                        },

                    "waterResource": 500,
                    "foodResource": 500,
                    "REEResource"       : 200,
                    "population": 100,
                    "fleetOwner": [
                        {
                         "name": "easy",
                         "fighters": 100,
                         "bombers" : 100,
                         "cargo"   : 1
                        }]
                 }
                }
 
    # create a pointer to planets
    user["planets"] = [copy.deepcopy(planets["p1"]), copy.deepcopy(planets["p2"])]
    easy["planets"] = [copy.deepcopy(planets["p2"])]
    user["fleets"] = [copy.deepcopy(fleets["fleet2"]), copy.deepcopy(fleets["fleet1"])]


    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    menu()









