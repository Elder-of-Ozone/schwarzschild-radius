#!/usr/bin/python3
from UIView import UIView
import User
from Controller import Controller

"""
This class handles the Model-View-Controller. 

"""


class SchwarzRadDemo():

    def __init__(self):
        print("Initialising game")
        self.main()
        self.View = UIView()
        #self.User = User()
        self.Controller = Controller(View, User)
        #self.Timer = TimeManager()

        self.main() 

    def main(self):
        
        while True:
            ret = self.Controller.updateView()
            if ret == 0:
                break

    def loadSettings():
        """
        What settings will there be?  
        """
        print("Load user settings")

    def loadUserData():
        """
        Loads user data        
        """

    def saveUserData():
        """
        Saves user data
        """

if __name__ == '__main__':
    demo = SchwarzRadDemo() 
