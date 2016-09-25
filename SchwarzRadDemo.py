#!/usr/bin/python3
from UIView import UIView
from User import User
from Controller import Controller
from TimeContainer import TimeContainer
"""
This class handles the Model-View-Controller. 

"""


class SchwarzRadDemo():

    def __init__(self):
        print("Initialising game")
        self.View = UIView()
        self.User = User()
        self.Time = TimeContainer()
        self.Controller = Controller(self.View, self.User, self.Time)
        
        self.main() 

    def main(self):
        
        while True:
            ret = self.Controller.updateView()
            if ret == 0:
                break


if __name__ == '__main__':
    demo = SchwarzRadDemo() 
