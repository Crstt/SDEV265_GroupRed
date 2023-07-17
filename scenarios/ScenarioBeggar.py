import random
import scenarioManager

class ScenarioBeggar(scenarioManager.Scenario):
    def __init__(self, gui, player, name, description, choices):
        super().__init__(gui, player, name, description, choices)
    
    def run(self, choice):
        print(f"Running scenario {self.name}...")
        print(self.description)

        #choice = int(input("1 for forest or 2 for plains: "))
        if(self.player.money>=100):
            if choice == 1:
                self.mod.distance = random.randint(16,32) #Travel fowrard 
                self.mod.money=-100
                self.mod.result = "You gave the beggar some money, and you continuted on your way."
                #print("Nothing happens today. You traveled one step closer to the next town and used one day's food ration.")
            else:
                if random.randint(1,100) <= self.player.huntAdjust:
                    self.mod.result = "The beggar threw a python at you in rage! Luckily, it missed you and slithered away. You're completely unharmed, and ran away successfully."
                    #print("You got lost. You did not travel much closer today.")
                else:
                    self.mod.result = "The beggar threw a python at you in rage! It bit you, and you died."                
                    #print("You ran into a python in the wilderness, got bitten, and died")
                    self.mod.death = True #You died, game over.
        else:
            self.mod.distance = random.randint(16,32) #Travel fowrard 
            self.mod.food = 10
            self.mod.result = "Seeing that you have no money, they beggar gives you a little bit of food to help you on your way."

        return self.mod