from FleetStatistics import FleetStatistics
import sys, os, random
from collections import Counter

#from buildings import buildings

class Logic:



    """
    The console is merely the game logic. Here includes  all main functions
    including moving, building, the queue handler and perhaps notifications*?
    
    *Although notifications will need another class
        - learn about thread safety
        - just merely using read only data.

    """
    ErrFile = None


    ATTACK  = 0
    DEFENSE = 1
    BONUS   = 2

    def __init__(self, user):
        self.user = user
    def updateQueue(self):
        
        for fleet in self.user["fleetQueue"]:
            self.move(fleet, fleet["destination"], True)
            return True
   
        for build in self.user["buildQueue"]:
            print("")

    def build(self, building, planet, quantity, time=4, begin=True):
        """testing
        """ 
        
        if begin == True:
            time = 4
            b1 = [building, planet, quantity, time]
            self.user['buildQueue'].append(b1)
       
                
            
        self.user['buildQueue'][0][3] -=1

        if time==0:
            buildings.builds(building, quantity, self.user, planet, time)
            del self.buildQueue[0]


    # probably one of the best written functions.
    def move(self,fleet, destination, inQueue = False):
        
        if fleet["time"] == 0:
            fleet["time"] = 5 #This will need to be put in a function for varying planets
            self.user['fleetQueue'].append(fleet)

        fleet["destination"] = destination
        fleet["time"] = fleet["time"]-1

        if fleet["time"] == 0:
            self.user['fleetQueue'].remove(fleet)
            fleet["origin"] = destination
            fleet["destination"] = None

    def invade(self, fleet, enemy, planet):
        
        enemyFleet = [fleet for fleet in planet["fleets"] if enemy["name"] == planet["owner"]]
 
        if not enemyFleet:
            print("planet can be invaded.")
        else:
            print("planet cannot be invaded")
            print(" This is because of %s still has:" % enemy["name"] )
            print(enemyFleet[0]["fleet"])
            
            #self.build(build[0], build[1], build[2], build[3], False)
    
        #def printStatistics():

    def printStatistics(self, opponent, defender):
        print("\n--------------------")
        print("Your ships")
        for key, ship in opponent.items():
            print("%s: %s" % (key, ship))

        
        print("\nEnemy ships")       
        for key, ship in defender.items():    
            print("%s: %s" % (key, ship))
        print("--------------------")


    def attackFleet(self, offender, defender):
        """
        Combat should be simultaneous and therefore calculations can't be applied to results in situ.
            self.build(build[0], build[1], build[2], build[3], False)
        
        Our first task is to calculate bonus attack (atk) points (always > 0) and then bonus defense (def) points.

        

        """

        defenderOld = defender
        offenderOld = offender
        
        self.printStatistics(offender["fleet"], defender["fleet"])

        def __attack__(offender, defender):

            # loops players and ships
            for ship, dict1 in FleetStatistics.AirAttack.items():
                for ship1, statList in dict1.items():
                    
                    # set up bonus scheme
                    atkBonus = 0
                    if offender["fleet"][ship] > 0:
                        for i in range(0, offender["fleet"][ship]):
                            if statList[self.ATTACK] == 0:    
                                # attack bonus is calculated differently
                                if random.randrange(0,100) <= 5: #statList[self.BONUS]:
                                    atkBonus +=1 

                            else:
                                if random.randrange(0,100) <= 5: #statList[self.BONUS]:
                                    atkBonus += statList[self.ATTACK] + 1
                    
                    
                        #let's make things less complicated for testing purposes.
                        #atkBonus = 0              
                        defBonus = 0 
                        
                        #print(offender[offShips])
                        bonus = (atkBonus - defBonus)
                        print("%d: critical hit on %s from %s" % (bonus ,ship1, ship))
                        #if bonus > 0:
                        #    bonus = 0
                        shipDamage = defender["fleet"][ship] - defender["fleet"][ship1]# - bonus
                        
                        defender["fleet"][ship] = shipDamage
                        
                        if defender["fleet"][ship] < 0:
                            defender["fleet"][ship] = 0


            return defender 


                       #self.logErrMsg("Something went wrong. Something will always inevitably go wrong.")
        offender = __attack__(defender, offender)
        defender    = __attack__(offender, defender)
        #defender    = defenderOld


       
        self.printStatistics(offender["fleet"], defender["fleet"])


    def logErrMsg(self,msg):
        print("Err Printed")

        if os.path.exists('err.log'):
            ErrFile = open("err.log","a")
            ErrFile.write(msg)
            ErrFile.write("\n")
            ErrFile.close()
        else:
            ErrFile = open("err.log", 'w')
            ErrFile.write(msg)
            ErrFile.write("\n")
            ErrFile.close()

            
