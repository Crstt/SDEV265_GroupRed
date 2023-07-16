from checkpoints.checkpoint import *
from scenarioManager import *

class CheckpointManager:
    # inputHoldVariable is to control the game while waiting for input, -1 is to hold and not do anything with it
    inputHoldVariable = -1
    def __init__(self, checkpoints,scenarioManager,player):
        self.checkpoints = checkpoints
        #to track where we're at, the state of the player within the checkpoints
        self.currentCheckpoint = checkpoints[0]
        self.scenarioManager = scenarioManager
        self.player = player

        #cost of ferry, Merchant pays .9* as much, scenarios currently use magic numbers for the cost
        self.ferryCost=150
        #initialize the player distance to next
        player.distNext=self.currentCheckpoint.distToNextCP
    
    #checkpoints are linear, so this will advance one checkpoint forward. if the checkpoint manager is already at the last checkpoint, call the gameover scenario
    def nextCheckpoint(self):
        print("Updating checkpoint manager state...")
        #if the player has no distance left to the checkpoint, advance to the next checkpoint
        if(self.player.distNext <= 0):
            indexOfCurrentCheckpoint = self.checkpoints.index(self.currentCheckpoint)
            indexOfCurrentCheckpoint +=1
            if(indexOfCurrentCheckpoint == len(self.checkpoints)):
                #final checkpoint, game is over
                print("Game over!")
                self.scenarioManager.gui.showEndScreen()
                #self.scenarioManager.callScenarioByName("Game Over")
            else:
                self.currentCheckpoint=self.checkpoints[indexOfCurrentCheckpoint]
                #player disToNextCP can be updated
                self.player.distNext=self.currentCheckpoint.distToNextCP
                #call the river() or town() menus once arriving at a new checkpoint
                #once there the gui is ready to display choices these wont need to do a terminal
                if self.currentCheckpoint.isRiver :
                    print("Should be a \"calling scenario River \" here")
                    self.scenarioManager.callScenarioByName("River")
                    self.player.distNext = self.currentCheckpoint.distToNextCP
                else:
                    self.townScenario()
                    self.player.distNext = self.currentCheckpoint.distToNextCP
                
        else:
            #player still has distance to go, call the player. travel checkpoint
            while(self.player.distNext >= 0):
                #if the palyer hits 0 distance to the next checkpoint, this will call nextCheckpoint again to pull up river or town scenarios
                self.scenarioManager.callRandomScenario()
            
            self.nextCheckpoint()
    #if default choice of -1 is used, use a terminal to poll choices
    #if choice isn't -1, then the input comes from a GUI selection and thus a specific scenario can be called directly from the scenario manager
    def townScenario(self,choice = -1):
        if(choice==-1):
            loopTillValidInput = True
            while loopTillValidInput:
                try:
                    print("You are at",self.currentCheckpoint.name+".","What would you like to do?\n1-Continue on the Trail\n2-Buy more supplies")
                    playerChoice = int(input())
                    if(playerChoice == -1):
                        #debug option
                        break
                    if(playerChoice==1):
                        self.scenarioManager.callScenarioByName("Travel")
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        self.scenarioManager.callScenarioByName("buySupplies")
                        loopTillValidInput=False
                    else:
                        print("Please try again.")
                except Exception as e: 
                    print("Invalid Input. Please try again.")
                    print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
                    #comment out below as needed
                    print(str(e))
        else:
            if(choice==1):
                self.scenarioManager.callScenarioByName("Travel")
                loopTillValidInput=False
            elif(choice==2):
                #TODO: when the GUI is ready call something to prompt for the amount of food
                self.scenarioManager.callScenarioByName("buySupplies")
                loopTillValidInput=False

    def nextScenario(self):
        print(f"Distance to the next scenario {self.player.distNext}")
        if self.player.distNext <= 0:
            self.nextCheckpoint()
            print("Checkpoint reached, calling next checkpoint")
        else:
            self.scenarioManager.callRandomScenario()

def createCheckpointList():
    #these locations can be found in the game mechanics doc
    checkpointList = []
    startCheckpoint = Checkpoint(False,20,"Start Place","Images/market/01.jpg")
    checkpointList.append(startCheckpoint)

    riverCheckpoint1 = Checkpoint(True,20,"River 1")
    checkpointList.append(riverCheckpoint1)

    townCheckpoint1 = Checkpoint(False,20,"Python Junction")
    checkpointList.append(townCheckpoint1)

    riverCheckpoint2 = Checkpoint(True,20,"River 2")
    checkpointList.append(riverCheckpoint2)

    townCheckpoint2 = Checkpoint(False,20,"Bear City")
    checkpointList.append(townCheckpoint2)

    riverCheckpoint3 = Checkpoint(True,20,"River 3")
    checkpointList.append(riverCheckpoint3)

    townCheckpoint3 = Checkpoint(False,20,"Gold Creek")
    checkpointList.append(townCheckpoint3)

    riverCheckpoint4 = Checkpoint(True,20,"River 4")
    checkpointList.append(riverCheckpoint4)

    finishCheckpoint = Checkpoint(False,0,"Finish")
    checkpointList.append(finishCheckpoint)
    return checkpointList

    