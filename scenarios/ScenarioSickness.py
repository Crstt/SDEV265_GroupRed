import random
import scenarioManager

class ScenarioSickness(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        roll = random.randint(1,100)
        
        if roll >= 50:
            self.mod.result = "You feel better tonight. You think you can travel tomorrow."
            self.mod.sick = False
        if roll > 10 and roll < 50:
            self.mod.result = "You feel worse tonight. You think you cannot travel tomorrow either."
            self.mod.sick = True
        if roll <= 10:
            self.mod.result = "You died of dysentery during the night."
            self.mod.sick = True
            self.mod.death = True

        return self.mod    