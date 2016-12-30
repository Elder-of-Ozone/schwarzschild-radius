#!/usr/bin/python3
from UIView import UIView
from FrontEnd import FrontEnd
from User import User
from Controller import Controller
from TimeContainer import TimeContainer
import argparse
"""
This class handles the Model-View-Controller.

"""


class SchwarzRadDemo():

    def __init__(self):
        print("Initialising game")
        self.View = UIView()
        self.FrontEnd = FrontEnd()
        self.FrontEnd.main()
        self.User = User()
        self.Time = TimeContainer()

        parser = argparse.ArgumentParser(description='Schwarzchild Radius')
        parser.add_argument('-g', action='store_false',
                                               help='Disables graphical user interface')
        args = parser.parse_args()

        print(args.g)

        if args.g:
            self.Controller = Controller(self.FrontEnd, self.User, self.Time)
        else:
            self.Controller = Controller(self.View, self.User, self.Time)


if __name__ == '__main__':
    demo = SchwarzRadDemo()
