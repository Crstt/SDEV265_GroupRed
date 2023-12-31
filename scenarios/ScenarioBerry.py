import random
import scenarioManager

class ScenarioBerry(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        #choice 1 is to eat the berries, 2 is to not eat the berries. 
        if choice == 1:            
            if random.randint(1,100)>= self.player.huntAdjust:
                self.mod.food -= random.randint(3,5)
                self.mod.result = "You got sick from the berries and vomitted. This costs you an extra day's of food rations"                
            else:
                self.mod.food += random.randint(5,15)   
                self.mod.result = f"You decided to collect the berries. You gained {self.mod.food} pounds of food."
        else:
            self.mod.distance = random.randint(16,32) #Travel fowrard 
            self.mod.result = "You've decided to not eat the berries you have found in the wild, you rely on the rations you have for now. "

        return self.mod