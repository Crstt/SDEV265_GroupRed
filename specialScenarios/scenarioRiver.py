import random
import scenarioManager

class ScenarioRiver(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
        self.ferryCost=150

    def run(self, choice):
        print("Running scenario code...")
        #Eventually call openPopUp() to fetch the river choice from the GUI rather than terminal, and remove the terminal code

        #choice = self.openPopUp()
        #if default choice of -1 is used, use terminal to poll choices
        #if choice isn't -1, then the input comes from a GUI selection and thus a specific effect can be done straight from the

        #TODO add a check for if the player has enough money to buy the ferry
        if True:
            #print("You are at a river. What would you like to do?\n1-Attempt to ford the river\n2-Buy a ferry (150$)")
            
            # Ford river Choice
            if(choice==1):
                
                if random.randint(1,100) <= self.player.huntAdjust:
                    #successfully cross the river
                    self.mod.result = "You succesfully crossed the river!"
                    print("You succesfully crossed the river!")
                    self.mod.distance=-10
                    return self.mod
                else:
                    #do something bad
                    self.mod.result = "You drowned while crossing the river"
                    print("You drowned while crossing the river")
                    self.mod.death = True #You died, game over.
                    return self.mod

            # Pay for ferry choice Choice
            elif(choice==2):
                ferryCost = self.ferryCost
                if(self.player.character=="Merchant"):
                    ferryCost = ferryCost*.9

                self.mod.result = "You paid "+str(ferryCost)+"$ to cross the river. You have "+str(self.player.money)+"$ left."
                print("You paid "+str(ferryCost)+"$ to cross the river")
                    
                self.mod.money=-ferryCost                        
                self.mod.distance=-10
                return self.mod  
            
        else: #these choices are for when the gui has successfully prompted the user and the command line isnt needed 
            if(choice==1):
                
                badEvent = random.randint(1,20)
                #50% chance of bad thing happening
                if badEvent<=10:
                    #do something bad
                    return self.mod
                else:
                    #successfully cross the river
                    self.mod.distance=-10
                    return self.mod
            elif(choice==2):
                if(self.player.character=="Merchant"):
                    if(self.player.money>=self.ferryCost*.9):
                        loopTillValidInput=False
                        self.mod.money=-self.ferryCost*.9
                        self.mod.distance=-10
                        #cross the river
                        return self.mod  
                else:
                    if(self.player.money>=self.ferryCost):
                        self.mod.money=-self.ferryCost
                        #cross the river
                        self.mod.distance=-10 
                        return self.mod

    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here