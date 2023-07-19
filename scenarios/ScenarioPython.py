import random
import scenarioManager

class ScenarioPython(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        self.mod.result = f"You lost some food to pythons. You gained {self.mod.distance} pounds of food."
        self.mod.food -= random.randint(10,25)
        return self.mod 