class RiverCheckpoint:
    def __init__(self, isRiver=False, isTown=False, distNextCP=0):
        self.isRiver = isRiver
        self.isTown = isTown
        self.distNextCP = distNextCP
    
    def updateState(self):
        print("Updating checkpoint state...")
        # Implement the logic to update the state of the checkpoint here