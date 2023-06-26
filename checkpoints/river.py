class RiverCheckpoint:
    def __init__(self,distNextCP=0,name=""):
        self.isRiver = True
        self.isTown = False
        self.distNextCP = distNextCP
        self.name=name
    
    def updateState(self):
        print("Updating checkpoint state...")
        # Implement the logic to update the state of the checkpoint here