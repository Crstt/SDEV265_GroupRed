import random
class scenarioHunt:
    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        self.name = "Hunt"
        self.description = "You decided to hunt today. You see some deer in the distance."
        #self.choice = ["This text will describe choice1", "This text will describe choice 2"]
        self.choice = [] #This would be the for when a scenario has no choice option
        self.mod = self.Modifiers()

    class Modifiers:
        def __init__(self):
            self.food = 0  # Food consumed during the day
            self.distance = 0 # Travveled distance during the day
            self.money = 0  # No money spent
            self.death = False  # Did not die
    
    def run(self):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        if random.randint(1,100) <= self.player.huntAdjust:
                huntFood = random.randint(5,15)                  
                print(f"You successfully hunted a deer. You got {huntFood} pounds of meet")
                self.mod.food += huntFood
                
        else:
            print("The deer escaped. You did not get any food")

        return self.mod
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here