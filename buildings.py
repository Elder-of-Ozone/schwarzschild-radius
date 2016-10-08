class buildingFactory():
    """
    I'm still working on structure for buildings.

    Megastructures
    Dysons Sphere (ring)
        High power output - a function of science stat
        Contains housing
        Research facility 



    """
    def __init__(self,name, quantity=1):
                
        self.quantity = quantity

        # e.g [1,3,4,8,16,32 etc] 
        # Related variables and functions in class User()
        # - inQueue
        # + getTotalQueue()

        self.placeInQueue = [] # e.g [2, 4,6,10] Limit this size
        
        # Yo Future Aaron:
        # This is just a case statement.  You use a dictionary to 
        # route the function. If error arises probably just a typo somewhere.
        # 
        # You should also probably put this in a try and raise exception.
        # Remember to do it in the future!
        # 
        # Also Susan says "must love wife". 
        # 
        # See ya dude
        

        self.buildings = {
                     "city":        self.city(),
                     "mine":        self.mine(),
                     "farm":        self.farm(),
                     "shipyard":    self.shipyard(),
                     "housing":     self.housing(),
        }
        self.buildings[name] 
        
    @staticmethod
    def listOfBuildings():
        # temporary instance of buildingFactory()
        
        # Deleted bug
        # avoid calling anything in here buildings
        # same variable name buildings!

        # make temporary instance of self
        Temp = buildingFactory("city")
        planet_list = []

                # for buil, value in TempClass.buildings.items():
       #     planet_list.append(building)

        #return buildings
        for resource, value in Temp.buildings.items():
            planet_list.append(resource)

        return planet_list


    def increaseQuantity(self, quantity=1):
        
        for resource, value in self.outputDict.items():
            if (planet[resource] - value) > 0:
                planet[resource] -= value
            else:
                return False
        # if loop fails, it breaks and returns false
        self.quantity+=quantity

 

    def decreaseQuantity(self,quantity=1):
        self.quantity -=quanity

    def totalOutput(self,resource):
        print("this function should get the total output of the given resource per turn")
    
    def city(self):
        self.description = "The city is fundamental to a growing population, providing homes and work"
        self.outputDict = {"housing": 10000}
        self.construction = {"metal": 1000, "rareEarth": 250}

    def mine(self):
        self.description = "Mines primarily provide metals and rare earth mineral resources"
        self.inputDict = {"energy": 50}
        self.outputDict = {"metal": 200, "rareEarth": 100}
        self.construction = {"metal": 200, "rareEarth": 100} 

    def farm(self):
        self.description = "Farms provide food for population"
        self.inputDict = {}
        self.outputDict = {}
        self.construction = {}


    def shipyard(self):
        self.description = "Shipyard are necesary to build ships"
        self.inputDict = {}
        self.outputDict = {}
        self.construction = {}


    def housing(self):
        self.description = "Housing provide living space for the planets population"
        self.inputDict = {}
        self.outputDict = {}
        self.construction = {}


