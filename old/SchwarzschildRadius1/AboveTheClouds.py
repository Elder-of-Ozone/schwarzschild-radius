from FleetStatistics import FleetStatistics


class Mechanics():

    class start:
        def start(self):
            print("load player data")
            

    class player:

        def save(self):
            print "saving"

        def load(self):
            print "loading"

    class planets:
        def save(self):
            print "Saving planets"

        def load(self):
            print "loading planets"



class Attack():

    """
        air:
            fighters 1:1 ratio

        
        invade: 
            population 
                population  1:1 ratio
                military    3:1 ratio

            military
                population  3:1
                military    1:1

    """


    def air(self, offender, defender):
   
        print "Attackers ships", offender.fighters
        print "Defenders ships", defender.fighters


        if offender.fighters > 0 and defender.fighters > 0:

            defenderShipsLost = (offender.fighters * FleetStatistics.fighter.fighter.attack)
            offenderShipsLost = (defender.fighters * FleetStatistics.fighter.fighter.attack)

            defender.fighters -=defenderShipsLost
            offender.fighters -=offenderShipsLost
      

        if defender.fighters < 0:
            defender.fighters = 0
        if offender.fighters < 0:
            offender.fighters = 0


        print "Attacker damage taken", offenderShipsLost
        print "Defender damage taken", defenderShipsLost
    
        print "Ships Remaining"
        print "Attackers ships", offender.fighters
        print "Defenders ships", defender.fighters

                

    #player 1 is the invader
    #player 2 is the defender
    def invade(self, offender, defender):
        if defender.fighters == 0:
            defender.population -= offender.population

            if defender.population <= 0:
                print "offender has invaded"
                
            if offender.population <=0:
                print "offender has failed"


class Player():

    #def __init__(self):
        #Mechanics = Mechanics.player()
        #Mechanics.load()

    fighters = 752
    population = 1000




player1 = Player()
player1.fighters = 500

player2 = Player()
    
attack = Attack()
attack.air(player1, player2)



if __name__ == "__main__":
    Mechanics = Mechanics.player()
    
    user = Player()

















#Monday 10 o clock
#Malaga oxly 96 
