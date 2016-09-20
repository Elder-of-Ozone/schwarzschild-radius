class logic():
    
    #def __init__(self, user, planet, fleet):
        
    class planets():
        @staticmethod
        def invade():

            

            print "invade" 

        @staticmethod
        def canStartNew(planet, fleet):
            if planet["owner"] is None:
                if fleet["fleet"]["outpost"] > 0:
                    return True
                else:
                    return False
            else:
                return False

        @staticmethod
        def new(user, planet, fleet):
            if logic.planets.canStartNew(planet, fleet):
                user["planets"].append(planet)
                planet["owner"] = user
                fleet["fleet"]["outpost"] -= 1
            else:
                print "Cannot create outpost"

                
