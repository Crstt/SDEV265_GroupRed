import random
import scenarioManager
    
class ScenarioFoundNugget(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)

    def run(self):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.distance = random.randint(75, 125)
        print(f"You found a gold nugget in the stream. ${self.mod.distance} has been added to your cash")
        return self.mod    
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here