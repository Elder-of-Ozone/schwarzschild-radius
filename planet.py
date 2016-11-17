from buildings import buildingFactory

class planet():
    population = 1000
    name = ""
    metals = 2000
    rareEarth = 1000
    city = buildingFactory("city")
    mine = buildingFactory("mine")
    farm = buildingFactory("farm")
    housing = buildingFactory("housing")


    def __init__(self, name, population=1000):
        self.name = planet.isNameValid(name)
        self.populaton = population

    def isNameValid(name):
        return name
