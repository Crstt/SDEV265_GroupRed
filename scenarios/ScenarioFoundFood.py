import random
import scenarioManager
    
class ScenarioFoundFood(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)

    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        self.mod.distance = random.randint(16,32) #Travel fowrard 
        
        self.mod.food = random.randint(3, 5)
        self.mod.result = f"You found edible dead pythons in your food supplies. You gained {self.mod.food} pounds of food."
        return self.mod    
