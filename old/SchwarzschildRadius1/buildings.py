class buildings:

    @staticmethod
    def builds(building, quantity, player, planet, time, *kwargs):
        success = 0
        #planet = player['planets'][player['viewPlanetIndex']]

        for key in buildings.buildings[building]["cost"].keys():
            if planet['resource'][key] - (buildings.buildings[building]["cost"][key] * quantity) > 0:
                success +=1

        if success == len(buildings.buildings[building]["cost"]):
            for key in buildings.buildings[building]["cost"].keys():
                planet['resource'][key] -= buildings.buildings[building]["cost"][key]*quantity      

            planet['building'][building] +=quantity
            return True
        else:
            return False

    buildings = {"mine": {
                        "cost":  {
                                    "REE": 200,
                                    "water": 100
                                 },
                        "output": 100,
                        "requirements": None
                         },
                "farm": {
                        "cost": {
                                    "REE": 200,
                                    "water": 100
                                    
                                },
                        "output": 100,
                        "requirements": None
                        },
                "desalination": {
                        "cost": {
                                    "REE": 200,
                                    "water": 100
                                },
                        "output": 100,
                        "requirements": None
                        }

                }

    

