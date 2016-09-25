#!/usr/bin/python

from UIView import UIView

class Controller():
    
    def __init__(self, View, User, Time):

        self.View = View
        self.User = User
        self.Time = Time

    def updateView(self):
        ret = self.View.show_menu(self.User, self.Time)
        #self.View.menu(self.User, self.Time)

        if ret == "1":
            self.View.show_user(self.User)
        elif ret == "2":
            self.View.add_option(self.User, self.User.fleets, self.User.planets)
        elif ret == "3":
            self.View.add_option()
        elif ret == "u":
            self.updateServer()
        elif ret == "n":
            self.addArtificalTurn()
        else:
            return 0

    def evalTurn(self):

        print("eval'd turn")        

    def updateQueue(self):
        print("updated queue")


