import random
import os
import importlib
import sys

class ScenarioManager:
    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        self.scenarios = []
        self.specialScenarios = []

        # Path to the scenarios folder
        scenarios_folder = 'scenarios'
        self.scenarios = self.loadScenarios(scenarios_folder)

        # Path to the specialScenarios folder
        specialScenarios_folder = 'specialScenarios'
        self.specialScenarios = self.loadScenarios(specialScenarios_folder)

    def loadScenarios(self, scenarios_folder):

        loadedScenarios = []

        # Add the scenarios folder to the Python module search path
        sys.path.append(scenarios_folder)

        # Get a list of Python files in the scenarios folder
        files = [f for f in os.listdir(scenarios_folder) if os.path.isfile(os.path.join(scenarios_folder, f)) and f.endswith('.py')]

        # Iterate over the files
        for file in files:
            # Get the module name from the file name
            module_name = os.path.splitext(file)[0]

            # Import the module dynamically
            module = importlib.import_module(module_name)

            # Get the class name based on the module name (assuming the class name is the same as the file name)
            class_name = module_name            

            # Get the class object from the module
            if hasattr(module, class_name):
                class_obj = getattr(module, class_name)
                
                # Instantiate the class and add the object to the scenarios array
                loadedScenarios.append(class_obj(self.gui, self.player))
            
        # Remove the scenarios folder from the Python module search path
        sys.path.remove(scenarios_folder)
        return loadedScenarios
    
    def callRandomScenario(self):
        return self.callScenario(random.choice(self.scenarios))
    
    def callScenario(self, scenario):
        print(f"Calling scenario: {scenario.name}")
        mod = scenario.run()
        if mod.death:
            print("END GAME") 
            #TODO: finish developing the end game mechanic
            return mod
        self.player.food += mod.food        
        self.player.money += mod.money
        self.player.distNext += mod.distance

        self.player.food += self.eat() #the player always eats. Handaled by default by the manager
        return mod
    
    def callScenarioByName(self, scenarioName:str):

        for scenario in self.specialScenarios:
            if scenario.name == scenarioName:
                return self.callScenario(scenario)

        for scenario in self.scenarios:
            if scenario.name == scenarioName:
                return self.callScenario(scenario)
    
    def eat(self):
        ateFood = 0 - random.randint(3,5)
        print(f"You ate and used {-ateFood} pounds of food")
        return ateFood
