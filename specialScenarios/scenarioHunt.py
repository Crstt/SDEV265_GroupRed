class scenarioHunt:
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.name = "Hunt"
        self.description = "description"
        self.choice = ["choice1", "choice 2"]
        self.choice = []
    
    def run(self):
        print("Running scenario code...")
        
        return self.name
        # Implement the logic for the scenario here
    
    def openPopUp(self):
        print("Opening popup...")
        # Implement the logic to open a popup related to the scenario here