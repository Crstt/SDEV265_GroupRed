from checkpoints import *
from scenarioManager import *
class CheckpointManager:
    def __init__(self, checkpoints,scenarioManager):
        self.checkpoints = checkpoints
        #to track where we're at, the state of the player within the checkpoints
        self.currentCheckpoint = checkpoints[0]
        self.scenarioManager = scenarioManager
    
    #checkpoints are linear, so this will advance one checkpoint forward. if the checkpoint manager is already at the last checkpoint, call the gameover scenario
    def updateState(self):
        print("Updating checkpoint manager state...")
        # Implement the logic to update the state of the checkpoint manager here
        indexOfCurrentCheckpoint = self.checkpoints.index(self.currentCheckpoint)
        indexOfCurrentCheckpoint +=1
        if(indexOfCurrentCheckpoint == len(self.checkpoints)-1):
            #final checkpoint, game is over
            print("Game over!")
            self.scenarioManager.callScenario(self.scenarioManager,"Game Over")
        else:
            self.currentCheckpoint=self.checkpoints[indexOfCurrentCheckpoint]
            
    #if default choice of -1 is used, use terminal to poll choices
    #if choice isn't -1, then the input comes from a GUI selection and thus a specific scenario can be called directly from the scenario manager
    def riverScenario(self,choice = -1):
        #if default choice of -1 is used, use terminal to poll choices
        #if choice isn't -1, then the input comes from a GUI selection and thus a specific scenario can be called directly from the scenario manager
        if(choice==-1):
            loopTillValidInput = True
            while loopTillValidInput:
                print("You are at the",self.currentCheckpoint.name,"river. What would you like to do?\n1-Attempt to ford the river\n2-Buy a ferry (150$)")
                try:
                    playerChoice = int(input())
                    if(playerChoice == -1):
                        #debug option
                        break
                    if(playerChoice==1):
                        self.scenarioManager.callScenario(self.scenarioManager,"fordRiver")
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        self.scenarioManager.callScenario(self.scenarioManager,"buyFerry")
                        loopTillValidInput=False
                    else:
                        print("Please try again.")
                except Exception as e:
                    print("Invalid Input. Please try again.")
                    #comment out below as needed
                    print(str(e))
        else:
            if(choice==1):
                self.scenarioManager.callScenario(self.scenarioManager,"fordRiver")
            elif(choice==2):
                self.scenarioManager.callScenario(self.scenarioManager,"buyFerry")

    #if default choice of -1 is used, use a terminal to poll choices
    #if choice isn't -1, then the input comes from a GUI selection and thus a specific scenario can be called directly from the scenario manager
    def townScenario(self,choice = -1):
        
        if(choice==-1):
            loopTillValidInput = True
            while loopTillValidInput:
                print("You are at",self.currentCheckpoint.name+".","What would you like to do?\n1-Continue on the Trail\n2-Check your supplies\n3-Rest\n4-Buy more supplies")
                try:
                    playerChoice = int(input())
                    if(playerChoice == -1):
                        #debug option
                        break
                    if(playerChoice==1):
                        self.scenarioManager.callScenario(self.scenarioManager,"travel")
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        self.scenarioManager.callScenario(self.scenarioManager,"checkSupplies")
                        loopTillValidInput=False
                    elif(playerChoice==3):
                        self.scenarioManager.callScenario(self.scenarioManager,"rest")
                        loopTillValidInput=False
                    elif(playerChoice==4):
                        self.scenarioManager.callScenario(self.scenarioManager,"buySupplies")
                        loopTillValidInput=False
                    else:
                        print("Please try again.")
                except Exception as e: 
                    print("Invalid Input. Please try again.")
                    #comment out below as needed
                    print(str(e))
        else:
            if(choice==1):
                self.scenarioManager.callScenario(self.scenarioManager,"continueTrail")
                loopTillValidInput=False
            elif(choice==2):
                self.scenarioManager.callScenario(self.scenarioManager,"checkSupplies")
                loopTillValidInput=False
            elif(choice==3):
                self.scenarioManager.callScenario(self.scenarioManager,"rest")
                loopTillValidInput=False
            elif(choice==4):
                self.scenarioManager.callScenario(self.scenarioManager,"buySupplies")
                loopTillValidInput=False