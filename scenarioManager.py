from scenarios import *
import random

class ScenarioManager:
    def __init__(self, scenarios):
        self.scenarios = scenarios
    
    def callRandomScenario(self):
        random_scenario = random.choice(self.scenarios)
        self.callScenario(random_scenario)
    
    def callScenario(self, scenario):
        print(f"Calling scenario: {scenario}")
        # Implement the logic for the scenario here
    
    def modFood(self):
        # Implement the logic to modify food here
        pass
    
    def modDay(self):
        # Implement the logic to modify day here
        pass
    
    def modState(self):
        # Implement the logic to modify state here
        pass
