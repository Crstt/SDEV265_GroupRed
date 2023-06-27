import random
class Scenario01:
    def __init__(self, gui):
        self.gui = gui
        self.name = "01"
        self.description = "This text will describe the promt to the user"
        self.choice = ["This text will describe choice1", "This text will describe choice 2"]
        self.choice = [] #This would be the for when a scenario has no choice option
        self.mod = self.Modifiers()

    class Modifiers:
        def __init__(self):
            self.food = random.randint(3,5)  # Example attribute
            self.distance = 10  # Example attribute
            self.money = 0  # Example attribute
            self.death = False  # Example attribute
    
    def run(self, choiceIndex:int = -1):
        print("Running scenario code...")
        self.mod.food += 5
        return self.mod #TO-DO return an array/object of values (ex. food, distance, money, and death)
        # Implement the logic for the scenario here
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here