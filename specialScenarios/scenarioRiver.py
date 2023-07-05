import random
import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory
import scenarioManager
class scenarioRiver:
    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        self.name = "River"
        self.description = "You are at a river crossing, and you can ford the river or buy a ferry across."
        self.choice = ["Ford River", "Buy Ferry"]
        #self.choice = []
        self.mod = self.Modifiers()
        self.ferryCost=150

    class Modifiers:
        def __init__(self):
            self.food = 0 - random.randint(3,5)  # Example attribute
            self.distance = 0  # Example attribute
            self.money = 0  # Example attribute
            self.death = False  # Example attribute
    def setPlayer(self,player):
        self.player=player
    def run(self):
        print("Running scenario code...")
        #Eventually call openPopUp() to fetch the river choice from the GUI rather than terminal, and remove the terminal code
        choice = -1
        #choice = self.openPopUp()
        #if default choice of -1 is used, use terminal to poll choices
        #if choice isn't -1, then the input comes from a GUI selection and thus a specific effect can be done straight from the
        if(choice==-1):
            loopTillValidInput = True
            while loopTillValidInput:
                print("You are at a river. What would you like to do?\n1-Attempt to ford the river\n2-Buy a ferry (150$)")
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
                            return self.mod
                        else:
                            #successfully cross the river
                            self.mod.distance=-10
                            return self.mod
                        loopTillValidInput=False
                    elif(playerChoice==2):
                        if(self.player.character=="Merchant"):
                            if(player.money>=self.ferryCost*.9):
                                loopTillValidInput=False
                                self.mod.money=-self.ferryCost*.9
                                #cross the river
                                self.mod.distance=-10
                                return self.mod  
                        else:
                            if(self.player.money>=self.ferryCost):
                                self.mod.money=-self.ferryCost
                                loopTillValidInput=False
                                #cross the river
                                self.mod.distance=-10 
                                return self.mod
                    else:
                        print("Please try again.")
                except Exception as exception:
                    #this is so the whole program doesnt crash when prompting for user input
                    #do nothing so that the code can run
                    num = 1
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
                    if(player.money>=self.ferryCost*.9):
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