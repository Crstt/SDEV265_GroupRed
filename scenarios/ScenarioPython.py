import random
import scenarioManager

class ScenarioPython(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        self.mod.distance = random.randint(16,32) #Travel fowrard 
        
        self.mod.food -= random.randint(10,25)
        self.mod.result = f"You lost some food to pythons. You lost {-self.mod.food} pounds of food."
        return self.mod 