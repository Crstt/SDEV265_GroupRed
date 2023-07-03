from checkpoints import *
from scenarioManager import *
class CheckpointManager:
    
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
            if(indexOfCurrentCheckpoint == len(self.checkpoints)-1):
                #final checkpoint, game is over
                print("Game over!")
                self.scenarioManager.callScenarioByName("Game Over")
            else:
                self.currentCheckpoint=self.checkpoints[indexOfCurrentCheckpoint]
                #player disToNextCP can be updated
                self.player.distNext=self.currentCheckpoint.distToNextCP
                #call the river() or town() menus once arriving at a new checkpoint
                #once there the gui is ready to display choices these wont need to do a terminal
                if self.currentCheckpoint.isRiver:
                    self.riverScenario()
                else:
                    self.townScenario()
                
        else:
            #player still has distance to go, call the player. travel checkpoint
            self.scenarioManager.callScenarioByName("Travel")
            if(self.player.distNext <= 0):
                #if the palyer hits 0 distance to the next checkpoint, this will call nextCheckpoint again to pull up river or town scenarios
                self.nextCheckpoint()

        
            
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
                        self.scenarioManager.callScenarioByName("fordRiver")
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        if(self.player.character=="Merchant"):
                            if(player.money>=self.ferryCost*.9):
                                loopTillValidInput=False
                                self.player.money-=self.ferryCost*.9
                                self.scenarioManager.callScenarioByName("buyFerry")    
                        else:
                            if(self.player.money>=self.ferryCost):
                                self.player.money-=self.ferryCost
                                loopTillValidInput=False
                                self.scenarioManager.callScenarioByName("buyFerry")
                    else:
                        print("Please try again.")
                except Exception as e:
                    print("Invalid Input. Please try again.")
                    #comment out below as needed
                    print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
                    print(str(e))
        else:
            if(choice==1):
                self.scenarioManager.callScenarioByName("fordRiver")
            elif(choice==2):
                if(self.player.character=="Merchant"):
                    if(self.player.money>=self.ferryCost*.9):
                        #scenario is called, currently just moves user 10 distance
                        self.player.money-=self.ferryCost*.9
                        self.scenarioManager.callScenarioByName("buyFerry")
                    else: 
                        print("You don't have enough money for the ferry.")
                else:
                    if(self.player.money>=self.ferryCost):
                        #scenario is called, currently just moves user 10 distance
                        self.player.money-=self.ferryCost
                        self.scenarioManager.callScenarioByName("buyFerry")
                    else: 
                        print("You don't have enough money for the ferry.")

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
                        self.scenarioManager.callScenarioByName("Travel")
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        self.scenarioManager.callScenarioByName("rest")
                        loopTillValidInput=False
                    elif(playerChoice==3):
                        #
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
                self.scenarioManager.callScenarioByName("rest")
                loopTillValidInput=False
            elif(choice==3):
                #TODO: when the GUI is ready call something to prompt for the amount of food
                self.scenarioManager.callScenarioByName("buySupplies")
                loopTillValidInput=False