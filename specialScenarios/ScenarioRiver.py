import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory
import random
import scenarioManager


class ScenarioRiver(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
        self.ferryCost=150

    def run(self, choice):
        print(f"Running scenario {self.name}...")

        #TODO add a check for if the player has enough money to buy the ferry
        if True:
            
            # Ford river Choice
            if(choice==1):
                if random.randint(1,100) <= self.player.huntAdjust:
                    #successfully cross the river
                    self.mod.result = "You succesfully crossed the river!"
                    #print("You succesfully crossed the river!")
                    self.mod.distance=-10
                    self.mod.money=0
                    return self.mod
                else:
                    #do something bad
                    self.mod.result = "You drowned while crossing the river"
                    #print("You drowned while crossing the river")
                    self.mod.death = True #You died, game over.
                    return self.mod

            # Pay for ferry choice Choice
            elif(choice==2):
                ferryCost = self.ferryCost
                if(self.player.character=="Merchant"):
                    ferryCost = ferryCost*.9
                self.mod.money=-ferryCost    
                self.mod.result = "You paid "+str(ferryCost)+"$ to cross the river. You have "+str(self.player.money-ferryCost)+"$ left."
                #print("You paid "+str(ferryCost)+"$ to cross the river")        
                self.mod.distance=-10
                return self.mod  
            
    
    