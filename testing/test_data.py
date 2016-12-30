#!/usr/bin/python

import sys

sys.path.append("/home/hydrius/projects/schwarzschild-radius")

from User import User
from TimeContainer import TimeContainer
from Controller import Controller
from buildings import buildingFactory

class Testings():

    def __init__(self):
        self.User = User()
        self.turn = 1
        self.main = User.planets["1"]
        view = None
        self.Controller = Controller(view, User, TimeContainer)

    def printv(self,turn):
        #print("Turn", turn)
        #print(self.main.name)
        print("New Turn on planet:", self.main.name)
        print("population:", self.main.populaton)
        #print(self.main.resource["metals"])
        #This is prints out the queue object and remaining turns

        for queue in self.main.queue:
            print(queue[0], queue[1])
        #print(self.main.resource)
        #print(self.main.mine.quantity)

    def setup(self):
        self.main.queue = [[self.main.mine, 4], [self.main.farm,8], [self.main.housing, 12]]
        #self.main.populaton = 100
        self.main.housing.quantity = 10
    def loop(self):
        maxTurn = 250
        for i in range(maxTurn):
            self.printv(i)
            self.Controller.evalTurn()



if __name__ == "__main__":
    Test = Testings()
    Test.setup()
    Test.loop()



