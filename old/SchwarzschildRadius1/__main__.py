import curses, pickle, copy, sys
from AboveTheClouds import Mechanics
from TimeMechanics import TimeMechanics
from buildings import buildings
from fleet import fleets
from testData import Test_DATA
from console import Console

# curses.newwin(nlines, ncols, begin_y, begin_x)

def viewFleets(fleetBox):
    userPlanet  = user['planets'][user['viewPlanetIndex']]
    name = userPlanet["name"] 
    fleetBox.addstr(3, 2, "Available Fleets")
    
    for i, fleet in enumerate(user["fleets"]):
        try:
            if fleet["origin"] == name:
                fleetBox.addstr(4+i, 2,"%d. %s" % (i, fleet["name"]))
            elif fleet["origin"]["name"] == name:
                fleetBox.addstr(4+i, 2,"%d. %s" % (i, fleet["name"]))
        except:
            pass
    fleetIndex = fleetBox.getstr(2, 18)
    
    try:
        fleetIndex = int(fleetIndex)
        return fleetIndex
    except:
        pass

    fleetBox.clear()
    fleetBox.erase()
    fleetBox.refresh()
    
def fleetBox():
    width = 30
    lines = 15
    fleetBox = curses.newwin(lines, width, 7, (screenSize[1]/2)-(width/2))
    fleetBox.box()
    fleetBox.border(0)

    fleetIndex = viewFleets(fleetBox)
    fleetBox.clear()
    fleetBox.refresh()
    fleetBox.border(0)

    fleetBox.addstr(2, 2, "      Fleet Menu  ")

    fleetBox.addstr(4, 2, "      %s" % user["fleets"][fleetIndex]["name"])

    fleetBox.addstr(6, 2, "1. Add/Remove")
    fleetBox.addstr(7, 2, "2. Move")
    fleetBox.addstr(8, 2, "3. Pick Up/Drop")
    fleetBox.addstr(9, 2, "4. Change Fleet Name")
    fleetBox.addstr(10,2, "5. Attack")
    fleetBox.addstr(12,2, "6. View Available Fleets")

    fleetBox.refresh()
    fleetBoxChoices(fleetBox, user["fleets"][fleetIndex]["name"], fleetIndex)

def fleetBoxChoices(fleetbox, name, fleetIndex):
   
    while(True):
        try:
            x = int(fleetbox.getstr(2,18))
            break
        except:
            pass
    if x == 1:
        pass
    if x == 2:
        fleetbox.clear()
        fleetbox.refresh()
        fleetbox.border(0)

        fleetbox.addstr(2,2, "MOVE %s TO" % name)
        fleetbox.addstr(4,2, "Planet List.")
        for i,  planetName in enumerate(user['planets']):
            fleetbox.addstr(5+i,2,"%d. %s" % (i+1, planetName["name"]))
        while(True):
            try:
                dest = int(fleetbox.getstr())
                break
            except:
                pass
       
        console.move(user["fleets"][fleetIndex],user['planets'][0], user['planets'][int(dest)-1])

        #message = "MOVE %s %s" % (user["fleets"][fleetIndex]["name"], user["fleets"][dest-1]["name"])
        #Console.console(message, user, user["fleets"][fleetIndex], fleetIndex)
    if x == 3:
        pass
    if x == 4:
        pass
    if x == 5:
        pass
    if x == 6:
        del fleetbox
        fleetBox()
        
def sendToConsole(message, miniConsole, planet):

    #Small box
    ret = True
    if miniConsole == True:
        consoleBox = curses.newwin(5, screenSize[1], screenSize[0]-5,0)
        consoleBox.border(0)
        consoleBox.box()
        
        consoleBox.addstr(2,3, "Build %s Quantity:" % message)
         
        consoleBox.refresh()
        curses.echo() 
        quantity = consoleBox.getstr(2,30)
        try:
            console.build(message, planet, int(quantity))
            #ret = Console.console("BUILD %s %d" % (message, int(quantity)), user, planet)  
        except:
            consoleBox.addstr(2, 30, "Retry and ensure you've entered a number?")
            consoleBox.getch()

        if ret == False:
            console.addstr(2, 30, "Not enough resources. Maybe I should find out what you need?")

    if miniConsole == False:
        print "miniConsole"

    #larger box


def title():

    title1 = "  ______          ______ __             __  ___                    "
    title2 = " /_  __/____     /_  __// /_   ___     /  |/  /____   ____   ____  "
    title3 = "  / /  / __ \     / /  / __ \ / _ \   / /|_/ // __ \ / __ \ / __ \ "
    title4 = " / /  / /_/ /    / /  / / / //  __/  / /  / // /_/ // /_/ // / / / "
    title5 = "/_/   \____/    /_/  /_/ /_/ \___/  /_/  /_/ \____/ \____//_/ /_/  "
    
    title = [title1, title2, title3, title4, title5]
                                                  
    return title


def viewPlanet(index = 0):
    screen.clear()
    screen.border()
    
    if index >= len(user['planets']):
        index = 0
    userPlanet      = user['planets'][index]
    
    turns           = user['turns']
    name            = userPlanet['name']
    population      = userPlanet['population']
    water           = userPlanet['multi']['water']
    REE             = userPlanet['multi']['REE']

    debris          = userPlanet['resource']['debris']
    waterResource   = userPlanet['resource']['water']
    foodResource    = userPlanet['resource']['food']
    REEResource     = userPlanet['resource']['REE']

    mine            = userPlanet['building']['mine']
    farm            = userPlanet['building']['farm']
    desalination    = userPlanet['building']['desalination']





    # Planet List   
    planetListBox   = curses.newwin(screenSize[0],20,0,0)
    planetListBox.border(1)
    planetListBox.box()

    planetListBox.addstr(2,2, "Planet List.")
    for i,  planetName in enumerate(user['planets']):
        planetListBox.addstr(4+i,2,"%d. %s" % (i+1, planetName["name"]))


    
    # Planet Information
    planetInfoBox   = curses.newwin((screenSize[0]/2)+1,((screenSize[1]-20)/2),0,19)
    planetInfoBox.box()
    planetInfoBox.border(0)

    planetInfoBox.addstr(2,  2,  "     Planet Information")
    planetInfoBox.addstr(4,  2,  "Name:                   %s" % name)
    planetInfoBox.addstr(6,  2,  "Population:             %d" % population)
    planetInfoBox.addstr(7,  2,  "Water:                  %d" % waterResource)
    planetInfoBox.addstr(8,  2,  "Food:                   %d" % foodResource)
    planetInfoBox.addstr(9,  2,  "Rare Earth Elements:    %d" % REEResource)
    planetInfoBox.addstr(10, 2,  "Debris:                 %d" % debris)

    # Game Information
    gameInformationBox = curses.newwin(screenSize[0]/2, ((screenSize[1]-20)/2)+3, 0, ((screenSize[1]-20)/2+18)) 
    gameInformationBox.box()
    gameInformationBox.border(0)

    

    gameInformationBox.addstr(2, 2, "       Game Information")
    gameInformationBox.addstr(3, 2, "Time:                       %d" % time)
    gameInformationBox.addstr(4, 2, "Turns:                      %d" % turns)
    #gameInformationBox.addstr(5, 2, "Visible?                   %r" % planetVisible())


    # Building Information
    buildingInfoBox = curses.newwin((screenSize[0]/2+2), (screenSize[1]-20)/2, (screenSize[0]/2)-1,19) 
    buildingInfoBox.box()
    buildingInfoBox.border(0)

    buildingInfoBox.addstr(2,2, "         Buildings")
    buildingInfoBox.addstr(4,2, "M. Mine:               %d" % mine)
    buildingInfoBox.addstr(5,2, "F. Farm:               %d" % farm)
    buildingInfoBox.addstr(6,2, "D. Desalination:       %d"  % desalination)

    # Fleet Information

    fleetInfoBox = curses.newwin((screenSize[0]/2+2), ((screenSize[1]-20)/2)+3, screenSize[0]/2-1, ((screenSize[1]-20)/2+18)           )
    fleetInfoBox.box()
    fleetInfoBox.border(0)

    fleetInfoBox.addstr(2,2, "          Fleets")
    
    for i, fleet in enumerate(user["fleets"]):
        try:
            if fleet["origin"] == name:
                fleetInfoBox.addstr(4+i, 2, fleet["name"])
            elif fleet["origin"]["name"] == name:
                fleetInfoBox.addstr(4+i, 2, fleet["name"])
            else:
                pass
        except:
            pass

    screen.refresh()
    planetListBox.refresh()
    planetInfoBox.refresh()
    gameInformationBox.refresh()
    buildingInfoBox.refresh()
    fleetInfoBox.refresh()
   
    index = viewPlanetChoice(userPlanet)
    del planetListBox
    del planetInfoBox
    del gameInformationBox
    del buildingInfoBox
    del fleetInfoBox
    viewPlanet(index) 

def viewPlanetChoice(planet):
    x = screen.getch()

    if x == ord("+"):
        playerList = [user, easy]
        global time
        time = TimeMechanics.updateEVERYTHING(playerList, time, console)

    elif x == ord("m"):
        sendToConsole("mine", True, planet)
     
    elif x == ord("f"):
        sendToConsole("farm", True, planet)

    elif x == ord("d"):
        sendToConsole("desalination", True, planet)


    elif x == ord("F"):
        fleetBox()

    elif x == ord("q"):

        mainMenu()
    else:
        try:
            user['viewPlanetIndex'] = int(chr(x))-1
            return int(chr(x))-1
        except:
            pass

    return  user['viewPlanetIndex']




def mainMenu():
    screen.border(0)
    global time
    x = 0
    while x != ord('9') or x != ord('q'):
        menuTitle = title()

        for i, line in enumerate(menuTitle):
            screen.addstr(1+i,5, line)

    
        message = "Welcome Captain! We await your orders"
        

        screen.addstr(9,2,      "Please enter a number:")
        screen.addstr(10,2,     "1. View Planet")
        screen.addstr(11,2,     "2. View Fleet")
        screen.addstr(12,2,     "3. View Surrounding Planets")
        screen.addstr(13,2,     "4. Enter Orders (console)")
        screen.addstr(17,2,     "8. About")
        screen.addstr(18,2,     "q. Exit")
        
        screen.refresh()
        x = screen.getch() 
        if x == ord('1'):
            viewPlanet()
        
        if x == ord('2'):
            pass

        if x == ord('3'):
            pass        


        if x == ord('+'):
            playerList = [user,easy]
            time = TimeMechanics.updateEVERYTHING(playerList, time)


        if x == ord('q'):
            screen.refresh()
            sys.exit()
        
            
            break
    curses.endwin()
            
    

class CursesWindow(object):
    def __enter__(self):
        curses.initscr()

    def __exit__(self, *args):
        curses.endwin()


if __name__ == "__main__":

    


    ncurses = True
    GUI     = False
    newUser = False

    time    = 0

    user    = Test_DATA.user
    easy    = Test_DATA.easy

    planets = Test_DATA.planets
    fleets  =  Test_DATA.fleets


    listOfAllPlanets = Test_DATA.listOfAllPlanets

    user["planets"] = [copy.deepcopy(planets["p1"]), copy.deepcopy(planets["p2"])]
    easy["planets"] = [copy.deepcopy(planets["p2"])]
    
    user["fleets"]  = [copy.deepcopy(fleets["fleet2"]), copy.deepcopy(fleets["fleet1"])]

    console = Console(user,planets,fleets)

    if ncurses == True:
        with CursesWindow():

            screen = curses.initscr()
            curses.noecho()
            screen.clear()
            screen.border(0)
            screenSize = screen.getmaxyx()
            try:
                curses.wrapper(mainMenu())
            finally:
                curses.endwin()

    elif GUI == True:
        """
        Need to decide which GUI toolkit to use (Tkinter, PyGame, WVwidget, etc).
        """
        pass 
