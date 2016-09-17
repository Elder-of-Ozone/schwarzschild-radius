from datetime import datetime

class TimeContainer:
    def __init__(self, created, turn_old=1):
        self.created = TimeContainer.getCurrentTime() 
        self.testing = 0
        self.turn = self.getCurrentTurn()
    def updateServerCreation(self):
        self.created = TimeContainer.getCurrentTime()

    @staticmethod
    def getCurrentTime():
        return datetime.now()

    def secondsElapsed(self):
        current = TimeContainer.getCurrentTime()

        self.seconds = (current-self.created).total_seconds()
        return self.seconds
       
    def getCurrentTurn(self):
        return self.secondsElapsed() + self.testing 

    def increaseTurn(self):
        self.testing = self.testing + 10

         
