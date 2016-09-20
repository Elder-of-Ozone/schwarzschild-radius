from console import Console
from testData import Test_DATA
import copy

user = Test_DATA.user
easy = Test_DATA.easy

planets = Test_DATA.planets
fleets = Test_DATA.fleets

user["planets"] = [copy.deepcopy(planets["p1"]), copy.deepcopy(planets["p2"])]
easy["planets"] = [copy.deepcopy(planets["p2"])]

user["fleets"] =[copy.deepcopy(fleets["fleet2"]), copy.deepcopy(fleets["fleet1"])]


print "before"
print user["fleets"][0]


#print user["fleets"][1]


console = Console(user, planets, fleets)


# Moving fleet1 @ p1 to p2

message = "MOVE"
console.move(user["fleets"][0], user["planets"][1], user["planets"][0])
 
for i in range(1,6):
    print "\nAfter"
    console.updateQueue()
    print user["fleets"][0]
#print user["fleets"][1]

