class Ships(shipType=None):

    """
    This class describes the classes of fleets and their purpose.


    Scouts
    ------
    Scouts are drones that survey the galaxy and report if enemy ships
    or planets are nearby.


    Outposts
    --------
    Outposts are ships that are used to colonise other planets.
    - 2000 max population.
    - 10,000 per each material.

    Freighters
    ----------
    Freighters are for transport. Useful to have many to establish
    trade routes.
    - 100,000 per each material

    Bombers
    -------
    Bombers are useful to destroy planet defenses before they attack your main fleet.


    Strengths
    - Planet Defenses
    - Destroyer (requires 4)
    - Battleships (requires 16)

    Weaknesses
    - Fighters
    - Frigates
    - Dreadnaughts

    Fighters
    --------

    Strengths
    - Bombers

    Weaknesses
    - Frigates
    - Battleships


    Frigates
    --------

    Strengths
    - Fighters
    - Destroyers
    - Battleships

    Weaknesses
    - Dreadnaught


    Destroyers
    ----------

    Strengths
    - Battleships
    - Dreadnaughts

    Weaknesses
    - Frigates




    Battleships
    -----------
    Strengths
    Weaknesses
    
    Dreadnaughts
    ------------

    Strengths
    
    Weaknesses



    """

    def __init__(self)




        self.shipType = "Fighter"
        self.health = 2 # health per ship
        self.damage = 0 # culumative damage
        self.quantity = 1000
        self.totalHealth = self.health * self.quantity





    def updateQuantity():
        self.quantity = (self.totalHealth - self.damage) / self.health
