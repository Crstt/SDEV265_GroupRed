import random
import scenarioManager
    
class ScenarioFoundFood(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)

    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.distance = random.randint(3, 5)
        self.mod.result = f"You found edible dead pythons in your food supplies. You gained {self.mod.distance} food units."
        return self.mod    
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here