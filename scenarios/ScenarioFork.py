import random
class ScenarioFork:
    def __init__(self, gui, huntAdjust):
        self.gui = gui
        self.huntAdjust = huntAdjust
        self.name = "Fork"
        self.description = "There is a fork in the trail. Do you want to go right toward the forest or left toward the plains? "
        self.choice = ["This text will describe choice1", "This text will describe choice 2"]
        #self.choice = [] #This scenario has no choice availabe
        self.mod = self.Modifiers()

    class Modifiers:
        def __init__(self):
            self.food = 0  # Food consumed during the day
            self.distance = 0 # Travveled distance during the day
            self.money = 0  # No money spent
            self.death = False  # Did not die
    
    def run(self):
        print(f"Running scenario {self.name}...")
        print(self.description)

        choice = int(input("1 for forest or 2 for plains: "))
        if choice == random.randint(1,2):
            if random.randint(1,100) <= self.huntAdjust:
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