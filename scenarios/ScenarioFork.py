import random
import scenarioManager

class ScenarioFork(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choice):
        super().__init__(gui, player, name, description, choice)
    
    def run(self):
        print(f"Running scenario {self.name}...")
        print(self.description)
        print("1 for forest or 2 for plains: ")
        choice = int(input("1 for forest or 2 for plains: "))
        if choice == random.randint(1,2):
            if random.randint(1,100) <= self.player.huntAdjust:
                print("You got lost. You did not travel much closer today.")
            else:                
                print("You ran into a python in the wilderness, got bitten, and died")
                self.mod.death = True #You died, game over.
        else:
            self.mod.distance = random.randint(16,32) #Travel fowrard 
            print("Nothing happens today. You traveled one step closer to the next town and used one day's food ration.")

        return self.mod 
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here