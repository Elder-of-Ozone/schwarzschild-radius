from console import Console as console
from testData import Test_DATA
import copy, json

from logic import logic
"""

Just a place to test new features.




"""
#import all user data
Test_DATA = Test_DATA()

user = Test_DATA.user
easy = Test_DATA.easy


planets = Test_DATA.generatePlanets()
fleets = Test_DATA.fleets

console = console(1,2,3)

#ensure everything is linked via pointers

user["planets"] = [copy.deepcopy(planets[0]), copy.deepcopy(planets[1])]
easy["planets"] = [copy.deepcopy(planets[2])]

user["fleets"] =[copy.deepcopy(fleets["fleet2"]), copy.deepcopy(fleets["fleet1"])]
easy["fleets"] = [copy.deepcopy(fleets["fleet2"])]

user["fleets"][0]["origin"] = copy.deepcopy(planets[0])
user["fleets"][1]["origin"] = copy.deepcopy(planets[1])

user["planets"][0]["fleets"] = copy.deepcopy(user["fleets"][0])
user["planets"][0]["fleets"] = copy.deepcopy(user["fleets"][0])

# Initial Settings

print "Welcome comrad!"
print "We are the Consortium."
print "Our aim is to uphold the galaxy's law and order."
print "You are soon ready to move up the ranks and join us."

#race = raw_input('What is the name of your race? ')
race = "Hydra"
#planet_name = raw_input ("what is the name of your planet? ")
planet_name = "whoami"

user['race'] = race
user['planets'][0]['name'] = planet_name 




#Set timer.


for time in xrange(0, 20):

    if time == 1:
        print "Time %d: Moving %s to %s" % (time, easy["fleets"][0]["name"], user["planets"][0]["name"])
        console.move(easy["fleets"][0], user["planets"][0]) 
        
    if easy["fleets"][0]["destination"] == user["planets"][0]:
        print "Time %d: fleet2 arrived" % time
print "Simulation Over."

#print easy["fleets"]



# * TURN 1 * 
# set common enemy fleet to home planet




#print planets[3]
#logic.planets.new(user, planets[3], user["fleets"][0])
#print user["fleets"]
        
#console = Console(user, planets, fleets)


# Moving fleet1 @ p1 to p2

#message = "MOVE"
#console.move(user["fleets"][0], user["planets"][1], user["planets"][0])
 
#for i in range(1,6):
#    console.updateQueue()








