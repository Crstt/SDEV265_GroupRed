class TownCheckpoint:
    def __init__(self, distNextCP=0,name=""):
        self.isRiver = False
        self.isTown = True
        self.distNextCP = distNextCP
        self.name=name
        
    def updateState(self):
        print("Updating checkpoint state...")
        # Implement the logic to update the state of the checkpoint here