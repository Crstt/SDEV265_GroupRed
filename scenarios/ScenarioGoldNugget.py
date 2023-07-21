import random
import scenarioManager
    
class ScenarioGoldNugget(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)

    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)
        
        self.mod.money = random.randint(75, 125)
        self.mod.result = f"You found a gold nugget in the stream. ${self.mod.money} has been added to your cash"
        return self.mod    