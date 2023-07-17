from tkinter import *
class Checkpoint:
    def __init__(self,isRiver=True,distToNextCP=0,name="",imgPath="",foodCost=1):
        if(isRiver):
            self.isRiver = True
            self.isTown = False
        else:
            self.isRiver = False
            self.isTown = True
        self.distToNextCP = distToNextCP
        self.name=name
        self.imgPath = imgPath
        self.foodCost=foodCost
    
    def updateState(self):
        print("Updating checkpoint state...")
        # Implement the logic to update the state of the checkpoint here