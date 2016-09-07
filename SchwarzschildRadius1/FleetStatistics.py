class FleetStatistics():

    # order is from strongest to weakest ships
    spaceships = ["fighter", "bomber", "outpost"]
    

    AirAttack = { 
             
            "fighters": 
                {
                    # list is [Attack, Defense, Bonus]
                    "fighters": [1, 1, 25],
                    "bomber" : [2, 1, 25],
                    "outpost": [2, 1, 25],
                },

            "bomber": 
                {
                    "fighters": [0, 1, 25],
                    "bomber" : [1, 1, 25],
                    "outpost": [1, 1, 25],
                },
            
            "outpost": 
                {
                    "fighters": [1, 1, 25],
                    "bomber" : [1, 1, 25],
                    "outpost": [1, 1, 25],
                }
        } 

    #groundAttack = dict{} //similar to above



    fighterAttack = [1,2,2]
    bomberAttack  = [0,2,2]
    outpostAttack = [0,1,1]

    
    
    class fighter:
        class fighter:
            attack = 1
            defense = 1
        class bomber:
            attack = 2
            defense = 2
        class cargo:
            attack = 2
            defense = 2

    class bomber:
        class fighter:
            attack = 1
            defense = 1
        class bomber:
            attack = 1
            defense = 1
        class cargo:
            attack = 1
            defense = 1
        class shields:
            attack = 3
            defense = 1

 
    class cargo:
        personel = 100

        class fighter:
            attack = 0
            defense = 1
        class bomber:
            attack = 0
            defense = 1
        class cargo:
            attack = 0
            defense = 1

     
