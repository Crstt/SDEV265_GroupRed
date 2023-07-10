import random
import scenarioManager

class ScenarioBison(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)
    
    def run(self):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.distance = random.randint(16,32)
        print(f"You travveled {self.mod.distance} miles today")
        return self.mod 
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here