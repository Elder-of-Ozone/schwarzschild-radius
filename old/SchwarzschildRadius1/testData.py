
class Test_DATA:

    #
    #
    #   Player Data
    #
    #


    user = {
                "name"              :           "Hydrius",
                "planets"           :           None,
                "fleets"            :           None,
                "turns"             :           100,
                "viewPlanetIndex"   :           0,
            }


    easy = {
                "name"              :           "easy",
                "planets"           :           None,
                "fleets"            :           None,
                "turns"             :           100,
            }


    medium =    {}
    hard   =    {}


    #
    #
    #   Planet       
    #
    #



    planets = {
                "p1":   {
                            "index"             :   0,
                            "name"              :   "p1",
                            "owner"             :   "hydrius",
                            "population"        :   100,
                            "multi"        :   {
                                                        "water" : 3,
                                                        "REE"   : 3
                                                    },
                            "resource"          :   { 
                                                        "debris"        :   100,
                                                        "water"         :   500,
                                                        "food"          :   500,
                                                        "REE"           :   200,
                                                    },

                            "building"          :   {   
                                                        "mine"          :   1,
                                                        "farm"          :   1,
                                                        "desalination"  :   1,
                                                    },
                        },

                "p2":   {
                            "name"              :   "p2",
                            "owner"             :   "hydrius",
                            "population"        :   100,
                            "multi"             :
                                                    {
                                                        "REE"      :   3,
                                                        "water"    :   3,
                                                    },

                            "resource"          :   { 
                                                        "debris"        :   100,
                                                        "water"         :   500,
                                                        "food"          :   500,
                                                        "REE"           :   200,
                                                    },

                            "building"          :   {   
                                                        "mine"          :   1,
                                                        "farm"          :   1,
                                                        "desalination"  :   1,
                                                    },
                        },
              }


    def generatePlanets(self):
        
        listofNames = ["irrah", "Caph", "Algenib", "Schedar", "Mirach",
                "Achernar",
                "Almach",
                "Hamal",
                "Polaris",
                "Menkar",
                "Merope",
                "Alcyone",
                "Atlas",
                "Zaurak",
                "Aldebaran",
                "Rigel",
                "Capella",
                "Bellatrix",
                "Elnath",
                "Nihal",
                "Mintaka",
                "Arneb",
                "Alnilam",
                "Alnitak",
                "Saiph",
                "Betelgeuse",
                "Menkalinan",
                "Mirzam",
                "Canopus",
                "Alhena",
                "Sirius",
                "Adara",
                "Wezen",
                "Castor",
                "Procyon",
                "Pollux",
                "Scheat",
                "Markab"]
        planets = []
        for idx, name in enumerate(listofNames):
            planet = {
                    "id"            : idx,
                    "name"          : name,
                    "owner"         : None,
                    "population"    : 100,
                    "multi"         :
                                        {
                                            "REE"      :   3,
                                            "water"    :   3,
                                        },

                    "resource"      :   { 
                                            "debris"        :   100,
                                            "water"         :   500,
                                            "food"          :   500,
                                            "REE"           :   200,
                                        },

                    "building"      :   {   
                                            "mine"          :   1,
                                            "farm"          :   1,
                                            "desalination"  :   1,
                                        },
                    }
              

            planets.append(planet)
        return planets

    fleets = {
                "fleet1":   {
                                "name"          :   "fleet1",
                                "origin"        :   "p1",
                                "destination"   :   None,
                                "time"          :   0,
                                "departed"      :   False,
                                "fleet":    {
                                                "fighters"  : 20,
                                                "outpost"   : 1
                                            }    
                            },

                "fleet2":   {
                                "name"          :   "fleet2",
                                "origin"        :   "p2",
                                "destination"   :   None,
                                "time"          :   0,
                                "departed"      :   False,
                                "fleet":     {
                                                "fighters"  : 20,
                                                "outpost"   : 1
                                            }
                            }
             }

