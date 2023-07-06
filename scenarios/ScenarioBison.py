import random
class ScenarioBison:
    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        self.name = "Bison"
        self.description = "You saw some wild buffalo in the distance. They didn't bother you and you traveled along your way. "
        #self.choice = ["This text will describe choice1", "This text will describe choice 2"]
        self.choice = [] #This scenario has no choice availabe
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
        
        self.mod.distance = random.randint(16,32)
        print(f"You travveled {self.mod.distance} miles today")
        return self.mod 
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here