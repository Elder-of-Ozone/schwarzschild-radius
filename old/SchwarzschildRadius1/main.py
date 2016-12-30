import curses, curses.panel
import sys, os, math, copy
from testData import Test_DATA


class GUI():
    
    DOWN = 1
    UP   = -1
    LEFT = -1
    RIGHT = 1


    # Planet view options
    IDX_PLANET = 0



    def __init__(self):
      
        # Variables for game
        self.time = 0

        # Variables for menu

        self.optionRange = 0
        self.deltaOptions = 0
        
        #up down variables
        self.topLineNum = 0
        self.highlightLineNum = 0
        self.bottomLineNum = 0

        #left right variables
        self.focusedPanelNum = 0
        self.horozontalLineNum = 0
        self.maxPanels = 2

        self.planetViewOptions = []
        self.panelStack = {} 
 
        self.Test_DATA = Test_DATA()
        self.loadData()
        curses.wrapper(self.mainMenu)

    def terminalSize(self):
        self.screenSize = curses.getmaxyx()
        return True


    def loadData(self):
        self.user = self.Test_DATA.user

        self.planets = self.Test_DATA.generatePlanets()
        self.user["planets"] = copy.deepcopy(self.planets)
        self.fleets = Test_DATA.fleets

    def createWinAndPanel(self, name, l, h, y, x):

        win = curses.newwin(l, h, y, x)
        win.box()
        win.border(0)
        panel = curses.panel.new_panel(win)

        #does this do a deepcopy? Does the existing panel go into garbage?
        self.panelStack[name] = panel

        panel.top()
        panel.show()
        self.screen.refresh
        win.refresh()

        curses.panel.update_panels()

        return win, panel


    def cursesSetup(self):

        # @ TO DO
        # PRIORITY 5
        # Check and resize terminal
        # True  : correct size and continue
        # False : close
        if self.terminalSize():
            # reserved for late
            print True


        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)


    def displayPlanet(self, panelList):
        self.screen.clear()
        self.menuBox.addstr(8,8,"did it work")

        if self.focusedPanelNum == 0:
            idx = self.highlightLineNum + self.topLineNum
            self.focusedPlanetNum = idx 
        else:
            idx = self.focusedPlanetNum
            self.highlightLineNum = idx - self.topLineNum

        #for panel in panelList:

            #self.panelStack[panel].move(9,10)
            #self.panelStack[panel].bottom()
            #self.panelStack[panel].hide()
            #self.screen.refresh()
            #self.screen.clear()

        try:
            for panel in planetViewScreens:
                self.panelStack[panel].show()

        except:
            self.planetListBox, self.planetListPanel = self.createWinAndPanel("p_List", self.screenSize[0], 20, 0, 0)
            self.planetInfoBox, self.planetInfoPanel = self.createWinAndPanel("p_Info", (self.screenSize[0]/2), ((self.screenSize[1]-20)/2)+1, 0, 19)
            self.gameInfoBox, self.gameInfoPanel = self.createWinAndPanel("game_info",  (self.screenSize[0]/2),((self.screenSize[1]-20)/2)+1, 0, ((self.screenSize[1]-20)/2)+19 )
            self.buildingInfoBox, self.buildingInfoPanel = self.createWinAndPanel("building_info", (self.screenSize[0]/2)+1, ((self.screenSize[1]-20)/2)+1, (self.screenSize[0]/2)-1, 19)
            self.fleetInfoBox, self.fleetInfoPanel = self.createWinAndPanel("fleet_info", (self.screenSize[0]/2)+1, ((self.screenSize[1]-20)/2)+1, (self.screenSize[0]/2)-1, ((self.screenSize[1]-20)/2)+19)

            self.planetViewScreens = [self.planetListPanel,self.planetInfoPanel, self.gameInfoPanel, self.buildingInfoPanel, self.fleetInfoPanel]
        #self.planetListPanel.top()
        #self.planetListPanel.show()
        #self.planetListPanel.top()

        #probably redundant but .refresh() is needed. 
        for panels in self.planetViewScreens:
            if panels.hidden:
                panels.show()
                self.displayPlanetListPanel(self.planetListBox)
                self.displayPlanetInfoPanel(self.planetInfoBox, idx)
                panels.window().refresh()

        #self.planetViewScreens[self.focusedPanelNum].window().addstr(1,1, "focused, %d" % self.focusedPanelNum) 
        #self.planetViewScreens[self.focusedPanelNum].window().addstr(2,1, "line, %d" % self.horozontalLineNum)
        self.scrollFunc(self.planetViewScreens[self.focusedPanelNum].window(), function=[self.displayPlanetInfoPanel])
        

        self.displayPlanet(panelList) 

    def displayFleets(self):
        print True

    def displayFleets(self):
        print True

    def displayScanners(self):
        print True

    def exit(self):
        print True

    def displayabout(self):
        print True


    def terminalSize(self):
        self.screenSize = self.screen.getmaxyx()

        #if self.terminalSize[0] < 1000 and self.terminalSize[1] < 1000:
            #curses.resizeterm(20, 30)
        return True 
    #else:
         #   return True

    def logmessages(message):
        print message



    def scrollFunc(self, window, direction = ["up", "down", "left", "right"], **kwargs):

        window.keypad(1)
        c = window.getch()

        if c == curses.KEY_UP and "up" in direction:
            self.updown(self.UP)
            window.addstr(7,7,"%d" % self.highlightLineNum)
        elif c == curses.KEY_DOWN and "down" in direction:
            self.updown(self.DOWN)

        elif c == curses.KEY_LEFT and "left" in direction:
            self.leftright(self.LEFT)

        elif c == curses.KEY_RIGHT and "right" in direction:
            self.leftright(self.RIGHT)

        elif c == ord("\n"):
            # Pass functions for menu via kwargs.
            #try:
            try:
                kwargs["function"][self.highlightLineNum]([window])
            except Exception as e:
                window.addstr(1,1, str(e))
                pass
            #except IndexError:
            #    pass
            #    #kwargs["function"][self.focusedPanelNum](window,self.highlightLineNum)
            #except TypeError:
            #    pass
            #    #kwargs["function"][self.focusedPanelNum](window,self.highlightLineNum)
            #except AttributeError:
            #    pass
            #self.functionList[self.highlightLineNum](["menu"])

    def mainMenu(self, stdcsr):
        self.screen = stdcsr
        self.cursesSetup()
        self.menuBox, menuPanel = self.createWinAndPanel("menu", 15, 30, 1, 1)
        #self.menuBox = curses.newwin(15,30,1,1)
        #self.panel1 = curses.panel.new_panel(self.menuBox)
        curses.panel.update_panels()

        self.menuBox.box()
        self.menuBox.border(0)
        self.functionList = [self.displayPlanet]


        while True:
            self.displayMenu()
            self.bottom = 0
            self.scrollFunc(self.menuBox, function=self.functionList)

    def leftright(self, increment):
        nextPanNum = self.focusedPanelNum + increment
        self.maxPanels = len(self.planetViewScreens)

        print nextPanNum

#        if increment == self.LEFT and nextPanNum != 0:
#            self.horozontalLineNum +=self.LEFT
#            return

#        elif increment == self.RIGHT and nextPanNum == self.maxPanels:
#            self.horozontalLineNum +=self.RIGHT
#            return

        if increment == self.LEFT and nextPanNum != -1:
            self.focusedPanelNum = nextPanNum
        elif increment == self.RIGHT and nextPanNum < self.maxPanels:
            self.focusedPanelNum = nextPanNum


    def updown(self, increment):
        
        nextLineNum = self.highlightLineNum + increment

        # if next highlighted line is hidden, update the top line
        if increment == self.UP and self.highlightLineNum == 0   and self.topLineNum != 0:
            self.topLineNum += self.UP
            return
        elif increment == self.DOWN and nextLineNum == self.optionRange[1] and self.bottom != self.nOptions:
            self.topLineNum += self.DOWN
            return


        if increment == self.UP and (self.topLineNum != 0 or self.highlightLineNum != 0):

            #self.topLineNum +=self.UP
            self.highlightLineNum = nextLineNum

        elif increment == self.DOWN and self.highlightLineNum+1 != self.nOptions and self.bottom != self.nOptions:

            #self.topLineNum += self.DOWN
            self.highlightLineNum = nextLineNum

    def displayMenu(self):

        menuOptions = ["Planets", "Fleets", "Galaxy", "Scanners", "About", "Exit"]
        self.nOptions = len(menuOptions)
        self.optionRange = (0, self.nOptions)
        menuFunctions = []       

        top = self.topLineNum
        bottom = self.topLineNum+curses.LINES

        for index, line in enumerate(menuOptions):

            if index != self.highlightLineNum:
                self.menuBox.addstr(index+1, 1, line)
            else:
                self.menuBox.addstr(index+1, 1, line, curses.A_BOLD)

        self.menuBox.refresh()

  

    def displayPlanetListPanel(self, window):
        self.nOptions = len(self.planets)
        window.addstr(1,2,"Planet List")

        y, x = window.getmaxyx()

        top = self.topLineNum
        self.bottom = self.topLineNum + y - 4
        bottom1 = y - 4
        self.optionRange = (top, bottom1)

        for idx, planet in enumerate(self.planets[top:self.bottom]):

            linenum = self.topLineNum + idx

            if idx!= self.highlightLineNum or self.focusedPanelNum != 0:
                window.addstr(idx+3, 2, "%s" % (planet["name"]))
            else:
                window.addstr(idx+3, 2, "%s" % planet["name"], curses.A_BOLD)


    def displayPlanetInfoPanel(self, window, idx=0):

        planet          = self.user["planets"][idx]
        name            = planet["name"]
        population      = planet["population"]
        water           = planet['multi']['water']
        REE             = planet['multi']['REE']

        debris          = planet['resource']['debris']
        waterResource   = planet['resource']['water']
        foodResource    = planet['resource']['food']
        REEResource     = planet['resource']['REE']

        window.addstr(2,2, "    Planet Info")
        window.addstr(4,2, "Name        %s" % name)      
        window.addstr(6,2, "Population  %d" % population)

        



gui = GUI()

