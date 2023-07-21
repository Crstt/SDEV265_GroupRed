import random
import scenarioManager

class ScenarioTravelers(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.distance = random.randint(16,32)
        self.mod.food = random.randint(3, 15)
        self.mod.result = f"The travelers gave you {self.mod.food} pounds of food and you traveled {self.mod.distance} miles today"
        return self.mod 