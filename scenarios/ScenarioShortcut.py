import random
import scenarioManager

class ScenarioShortcut(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        if choice == 1:
            if random.randint(1,100) <= self.player.huntAdjust:
                self.mod.result = "You made it through successfully. You traveled much closer today."
                self.mod.distance = random.randint(16,32)*2 #Travel fowrard 
            else:
                self.mod.result = "You fell off a cliff and died"          
                self.mod.death = True #You died, game over.
        else:
            self.mod.distance = random.randint(16,32) #Travel fowrard 
            self.mod.result = "Nothing happens, you continued along your original journey."

        return self.mod