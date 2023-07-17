import random
import scenarioManager

class ScenarioHunt(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        if random.randint(1,100) <= self.player.huntAdjust:
                huntFood = random.randint(5,15)                
                self.mod.result = f"You successfully hunted a deer. You got {huntFood} pounds of meet"
                self.mod.food += huntFood
                
        else:
            self.mod.result = "The deer escaped. You did not get any food"

        return self.mod