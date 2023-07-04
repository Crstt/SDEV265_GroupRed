import random
class scenarioRiver:
    def __init__(self, gui, huntAdjust):
        self.gui = gui
        self.huntAdjust = huntAdjust
        self.name = "River"
        self.description = "description"
        self.choice = ["choice1", "choice 2"]
        self.choice = []
        self.mod = self.Modifiers()

    class Modifiers:
        def __init__(self):
            self.food = 0 - random.randint(3,5)  # Example attribute
            self.distance = 0  # Example attribute
            self.money = 0  # Example attribute
            self.death = False  # Example attribute

    def run(self):
        print("Running scenario code...")
        #Eventually call openPopUp() to fetch the river choice from the GUI rather than terminal, and remove the terminal code
        choice = -1
        #choice = self.openPopUp()
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
                        #call random to see if a bad event happens
                        badEvent = random.randint(1,20)
                        #50% chance of bad thing happening
                        if badEvent<=10:
                            #do something bad
                            return mod
                        else:
                            #successfully cross the river
                            self.mod.distance=-10
                            return mod
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        if(self.player.character=="Merchant"):
                            if(player.money>=self.ferryCost*.9):
                                loopTillValidInput=False
                                self.player.money-=self.ferryCost*.9
                                #cross the river
                                self.mod.distance=-10
                                return mod  
                        else:
                            if(self.player.money>=self.ferryCost):
                                self.player.money-=self.ferryCost
                                loopTillValidInput=False
                                #cross the river
                                self.mod.distance=-10 
                                return mod
                    else:
                        print("Please try again.")
                    
        else:
            #these choices are for when the gui has successfully prompted the user and the command line isnt needed 
            if(choice==1):
                badEvent = random.randint(1,20)
                #50% chance of bad thing happening
                if badEvent<=10:
                    #do something bad
                    return mod
                else:
                    #successfully cross the river
                    self.mod.distance=-10
                    return mod
            elif(choice==2):
                if(self.player.character=="Merchant"):
                    if(self.player.money>=self.ferryCost*.9):
                        #scenario is called, currently just moves user 10 distance
                        self.player.money-=self.ferryCost*.9
                        self.mod.distance=-10 
                        return mod
                    else: 
                        print("You don't have enough money for the ferry.")
                else:
                    if(self.player.money>=self.ferryCost):
                        #scenario is called, currently just moves user 10 distance
                        self.player.money-=self.ferryCost
                        self.mod.distance=-10 
                        return mod
                    else: 
                        print("You don't have enough money for the ferry.")

    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here