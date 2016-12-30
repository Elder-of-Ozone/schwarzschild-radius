from datetime import datetime

class TimeContainer:
    def __init__(self, created=1, turn_old=1):
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

    def addArtificalTurn(self):
        for x in range(0,self.testing):
            self.testing = self.testing + x
            evalTurn()

    def evalTurn(self):
        print("Evaluated turn")

