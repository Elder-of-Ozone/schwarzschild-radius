from buildings import buildings

class Console:

    """
    The console is merely the game logic. Here includes  all main functions
    including moving, building, the queue handler and perhaps notifications*?
    
    *Although notifications will need another class
        - learn about thread safety
        - just merely using read only data.

    """

    def __init__(self, user, planet, fleet):
        self.user = user
        self.planet = planet
        self.fleet = fleet
        self.fleetQueue = []
        self.buildQueue = []
        self.timesCalled = 0
         

#        self.times
        #called +=1 #no idea what to do with this. Stoned but might come in handy for the user

    def updateQueue(self):

        for fleet in self.fleetQueue:
            self.move(fleet, fleet["origin"], fleet["destination"], True)
            return True
   
        for build in self.buildQueue:
            print build[3]
            self.build(build[0], build[1], build[2], build[3], False)

    def build(self, building, planet, quantity, time=4, begin=True):
        if begin == True:
            time = 4
            b1 = [building, planet, quantity, time]
            self.buildQueue.append(b1)
       
        
            
        self.buildQueue[0][3] -=1

        if time==0:
            buildings.builds(building, quantity, self.user, planet, time)
            del self.buildQueue[0]


    # probably one of the best written functions.
    def move(self,fleet, destination, inQueue = False):
        if fleet["time"] == 0:
            fleet["time"] = 5 #This will need to be put in a function for varying planets
            self.fleetQueue.append(fleet)

        fleet["destination"] = destination
        fleet["time"] = fleet["time"]-1

        if fleet["time"] == 0:
            self.fleetQueue.remove(fleet)
            fleet["origin"] = destination
            fleet["destination"] = None

    def invade(self, origin, destination):
        print "invade"

    def console(self, message, fleetIndex = 0):     
        if message == "ATTACK":
            print "ATTACK"

        if message == "PICKUP":
            print "PICKUP"

        if message == "DROP":
            print "DROP"

        if message[0] == "BUILD":
            buildings.builds(message[1],  int(message[2]), user, planet)  
            print "BUILD"



#    def getIndexFromName(name, fleetOrPlanet = "planets"):
 #       for i in user[fleetOrPlanet]:
  #          if user[fleetOrPlanet]:

