from datetime import datetime

class TimeContainer:
    def __init__(self, created, turn_old=1):
        self.turn = turn_old
        self.created = TimeContainer.getCurrentTime() 

    def updateServerCreation(self):
        self.created = TimeContainer.getCurrentTime()

    @staticmethod
    def getCurrentTime():
        return datetime.now()

    def secondsElapsed(self):
        current = TimeContainer.getCurrentTime()

        seconds = (current-self.created).total_seconds()
        return seconds
       
    def getCurrentTurn(self):
        return self.secondsElapsed()

    def increaseTurn(self, turn):
        return turn + 10

         
