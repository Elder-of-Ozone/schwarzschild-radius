from buildings import buildings

class TimeMechanics():

   # def __init__(console):

    @staticmethod
    def updateEVERYTHING(playerList, time, console):
        
        

        #Will need to be for users planets!!!!
        for users in playerList:

            for planets in users['planets']:

                planets['population'] +=100
                planets['resource']['debris'] -= (planets['resource']['debris']/11)
                planets['resource']['water'] += planets['building']['desalination'] * planets['multi']['water'] * buildings.buildings['desalination']["output"]
                planets['resource']['food']  += planets['building']['farm'] * buildings.buildings['farm']['output']
                planets['resource']['REE']   += planets['building']['mine'] * planets['multi']['REE'] * buildings.buildings['mine']['output']
        time +=1
        console.updateQueue()

        
        return time



if __name__ == "__main__":

    TimeMechanics = TimeMechanics()
    






