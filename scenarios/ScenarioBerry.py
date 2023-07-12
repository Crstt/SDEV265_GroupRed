import random
import scenarioManager

class ScenarioBerry(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        #choice = int(input("1 for forest or 2 for plains: "))
        if choice == 1:
            if random.randint(1,100) <= self.player.huntAdjust:
                self.mod.result = "You got lost. You did not travel much closer today."
                print("You got lost. You did not travel much closer today.")
            else:
                self.mod.result = "You ran into a python in the wilderness, got bitten, and died"                
                print("You ran into a python in the wilderness, got bitten, and died")
                self.mod.death = True #You died, game over.
        else:
            self.mod.distance = random.randint(16,32) #Travel fowrard 
            self.mod.result = "Nothing happens today. You traveled one step closer to the next town and used one day's food ration."
            print("Nothing happens today. You traveled one step closer to the next town and used one day's food ration.")

        return self.mod 
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here