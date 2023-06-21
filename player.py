from random import random
from . import checkpointManager

class Player:
    miles = random(16,32)
    foodDaily = random(12,15)

    def __init__(self, character:str, money:int, food:int, huntAdjust:float, buyHudjust:float, distNext:int):
        self.character = character
        self.money = money
        self.food = food
        self.huntAdjust = huntAdjust
        self.buyAdjust = buyHudjust
        self.distNext = distNext

    def travel(self,didTravel=True, miles=miles, food=foodDaily):
        #call scenario
        if didTravel:
            self.distNext -= miles
            self.food -= food
            if self.distNext <=0:
                #call Checkpoint Manager
                checkpointManager

    def hunt(self, food=foodDaily):
        #call scenario hunt
        self.food -= food