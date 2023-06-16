class Scenario(ScenarioManager):
    def __init__(self, description, choice="none"):
        super().__init__([])
        self.description = description
        self.choice = choice
    
    def scenarioCode(self):
        print("Running scenario code...")
        # Implement the logic for the scenario here
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here