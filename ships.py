class Ships(shipType=None):
    def __init__(self)
        self.shipType = "Fighter"
        self.health = 2 # health per ship
        self.damage = 0 # culumative damage
        self.quantity = 1000
        self.totalHealth = self.health * self.quantity


    def updateQuantity():
        self.quantity = (self.totalHealth - self.damage) / self.health
