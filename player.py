import random
import csv

#from . import checkpointManager

class Player:
    miles = random.randint(16,32)
    foodDaily = random.randint(12,15)

    def __init__(self, character:str, money:int, food:int, huntAdjust:float, buyAudjust:float, distNext:int):
        self.character = character
        self.money = money
        self.food = food
        self.huntAdjust = huntAdjust
        self.buyAdjust = buyAudjust
        self.distNext = distNext

    def createPlayer():
        filename = "SDEV265_GroupRed/characters.txt"
        characters = {}
        with open(filename, 'r') as csvfile:
            for row in csv.reader(csvfile):
                characters[row[0]] = Player(*row[1:])
        return characters
    
characters = Player.createPlayer()
print (characters['Banker'].character)
print (characters['Banker'].money)
print (characters['Banker'].food)
print (characters['Banker'].huntAdjust)
print (characters['Banker'].buyAdjust)
print (characters['Banker'].distNext)

print (characters['Merchant'].character)
print (characters['Merchant'].money)
print (characters['Merchant'].food)
print (characters['Merchant'].huntAdjust)
print (characters['Merchant'].buyAdjust)
print (characters['Merchant'].distNext)

print (characters['Farmer'].character)
print (characters['Farmer'].money)
print (characters['Farmer'].food)
print (characters['Farmer'].huntAdjust)
print (characters['Farmer'].buyAdjust)
print (characters['Farmer'].distNext)
