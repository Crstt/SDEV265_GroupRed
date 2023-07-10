import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory
from checkpointManager import *
from checkpoints.town import *
from checkpoints.river import *
from gui import *
from player import *
#Tester

player1 = Player(*selectCharacter())

print("You are playing the " + player1.character)
print("You have $" + str(player1.money))
print("Your food suply is currently " + str(player1.food))
print("Your Hunt Adjusment is " + str(player1.huntAdjust) + "%")
print("Your buying adjustment is " + str(player1.buyAdjust) +"%")
print("The distance to the next checkpoint is " + str(player1.distNext) + " miles")

print("\nCreate some adjustments\n")
player1.distNext = 500
player1.food = 1000
player1.money = 550

print("You are playing the " + player1.character)
print("You have $" + str(player1.money))
print("Your food suply is currently " + str(player1.food))
print("Your Hunt Adjusment is " + str(player1.huntAdjust) + "%")
print("Your buying adjustment is " + str(player1.buyAdjust) +"%")
print("The distance to the next checkpoint is " + str(player1.distNext) + " miles")

print("\nCreate some adjustments\n")
player1.distNext -= 75
player1.food -= 10
player1.money -=50

print("You are playing the " + player1.character)
print("You have $" + str(player1.money))
print("Your food suply is currently " + str(player1.food))
print("Your Hunt Adjusment is " + str(player1.huntAdjust) + "%")
print("Your buying adjustment is " + str(player1.buyAdjust) +"%")
print("The distance to the next checkpoint is " + str(player1.distNext) + " miles")