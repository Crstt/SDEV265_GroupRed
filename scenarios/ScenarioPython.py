import random
import scenarioManager

class ScenarioPython(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        self.mod.result = "You lost some food to pythons."
        self.mod.food -= random.randint(3,5)
        return self.mod 