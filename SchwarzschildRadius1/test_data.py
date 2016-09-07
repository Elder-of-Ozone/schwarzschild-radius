
class test_data:

       
    planets = [
                {
                 
                                    "index"     : 0,
                                    "name"      : "hydrius' planet",
                                    "owner"     : "hydrius",
                                    "population" : "100",
                                
                },
                {    
                                    "index"     : 1,
                                    "name"      : "enemy's planet",
                                    "owner"     : "whatever",
                                    "population" : "100",
                }
            ]
     
    fleets = [
                {
                    "name"      :       "fleet1",
                    "owner"     :       "Hydrius",
                    "origin"    :       planets[0],
                    "destination":      None,
                    "time"      :       0,
                    "fleet"     :   
                                    {
                                        "fighters": 200,
                                        "bomber": 0,
                                        "outpost" : 1,
                                    },
                },
                
                {
                    "name"      :       "fleet2",
                    "owner"     :       "whatever",
                    "origin"    :       planets[1],
                    "destination":      None,
                    "time"      :       0,
                    "fleet"     :   
                                    {
                                        "fighters": 100,
                                        "bomber": 0,
                                        "outpost" : 1,
                                    },
                }
             ]

    user =  { 
                "name"          :           "Hydrius",
                "race"          :           "Hydra",
                "planets"       :           [planets[0]],
                "fleets"        :           [fleets[0]]
            }

    enemy = {
                "name"          :           "whatever",
                "race"          :           "whatever",
                "planets"       :           [planets[1]],
                "fleets"        :           [fleets[1]],
            }

                                                                                                                                                     


