import random
import csv
import os
import importlib
import sys

class Scenario:
    def __init__(self, gui, player, name, description, choice):
        self.gui = gui
        self.player = player
        self.name = name
        self.description = description
        self.choice = choice
        self.mod = self.Modifiers()

    class Modifiers:
        def __init__(self):
            self.food = 0  # Food consumed during the day
            self.distance = 0  # Traveled distance during the day
            self.money = 0  # No money spent
            self.death = False  # Did not die

class ScenarioManager:
    #creates a player object that every scenario can refer to without needing to pass it to the constructor
    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        globalPlayer = player
        self.scenarios = {}
        self.specialScenarios = {}

        # Path to the scenarios folder
        scenarios_folder = 'scenarios'
        self.scenarios = self.loadScenarios(scenarios_folder)

        # Path to the specialScenarios folder
        specialScenarios_folder = 'specialScenarios'
        self.specialScenarios = self.loadScenarios(specialScenarios_folder)

    def loadScenarios(self, scenarios_folder):

        # loadedScenarios = []
        scenarios_dict = {}

        # Add the scenarios folder to the Python module search path
        sys.path.append(scenarios_folder)

        scenarios_values_dict = self.loadFromCsv(scenarios_folder + "/scenarios.csv")  

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
                try:
                    name = class_name.replace("Scenario", "")
                    #loadedScenarios.append(class_obj(self.gui, self.player, name, scenarios_values_dict[name]['description'], scenarios_values_dict[name]['choice'])
                    scenarios_dict[name] = class_obj(self.gui, self.player, name, scenarios_values_dict[name]['description'], scenarios_values_dict[name]['choice'])
                except Exception as exception:
                    print(exception)
            
        # Remove the scenarios folder from the Python module search path
        sys.path.remove(scenarios_folder)
        return scenarios_dict
    
    def loadFromCsv(self, csv_path):
        scenarios_values_dict = {}
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                description = row['Description']
                choice1 = row['Choice 1']
                choice2 = row['Choice 2']
                if choice1 == "" and choice2 == "":
                    choice = []
                else:
                    choice = [choice1, choice2]


                # Add the scenario to the scenarios_values_dict dictionary
                scenarios_values_dict[name] = {
                    'description': description,
                    'choice': choice
                }

        return scenarios_values_dict
        
    def callRandomScenario(self):
        return self.callScenario(random.choice(list(self.scenarios.items()))[1])
    
    def callScenario(self, scenario):
        print(f"Calling scenario: {scenario.name}")
        mod = scenario.run()
        if mod.death:
            print("END GAME") 
            #TODO: finish developing the end game mechanic
            return mod
        self.player.food += mod.food        
        self.player.money += mod.money
        #this needs to subtract. checkpointManager calls when this is 0, the scenarios return a positive distance. if this is addition, checkpoint manager will infinite loop
        self.player.distNext -= mod.distance
        self.player.food += self.eat() #the player always eats. Handaled by default by the manager
        #input() # Stops the run of the game at each scenario TODO remove this
        return mod
    
    def callScenarioByName(self, scenarioName:str):
        if scenarioName in self.scenarios:
            return self.callScenario(self.scenarios[scenarioName])
        
        if scenarioName in self.specialScenarios:
            return self.callScenario(self.specialScenarios[scenarioName])
    
    def eat(self):
        ateFood = 0 - random.randint(3,5)
        print(f"You ate and used {-ateFood} pounds of food")
        return ateFood
