from logic import Logic
from test_data import test_data as test

#set up global thingys

t0 = 0
t_max = 10

user = test.user
bot = test.enemy

user["planets"][0]["fleets"] = [user["fleets"][0]]
bot["planets"][0]["fleets"] = [bot["fleets"][0]]

#print bot["planets"][0]


user["buildQueue"] = []
user["fleetQueue"] = []

Logic = Logic(user)



for time in range(t0, t_max):
    print("\nTime: %d\n" %time)
    
    if time == 0:
        print("Moving:\n")
        print(user["fleets"][0]["fleet"])
        print("TO:\n")
        print(bot["planets"][0]["name"])

        Logic.move(user["fleets"][0], bot["planets"][0])
   
    if time == 5:
        print("Attacking")
        #print(user["fleets"][0])
        Logic.attackFleet(user["fleets"][0], bot["planets"][0]["fleets"][0])

    if time == 6:
        Logic.invade(user["fleets"][0], bot, bot["planets"][0])

   #print(user["fleets"][0]["origin"]["name"])
    Logic.updateQueue()

#print(bot)




