import random
import scenarioManager
    
class ScenarioTravel(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)

    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.distance = random.randint(16, 32)
        #print(f"You traveled {self.mod.distance} miles today")
        self.mod.result = f"You traveled {self.mod.distance} miles today"
        return self.mod    
    