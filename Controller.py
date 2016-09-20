#!/usr/bin/python

class Controller():
    
    def __init__(self, View, User):

        self.View = View
        self.User = User

    def updateView(self):
       self.View.menu()

    def evalTurn(self):
        print("eval'd turn")        

    def updateQueue(self):
        print("updated queue")


