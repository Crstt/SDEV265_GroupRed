import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory
from checkpointManager import *
from checkpoints.town import *
from checkpoints.river import *
from gui import *
from player import *

#initialization of a checkpoint manager. These checkpoints are based on the design doc. Not intended for final use but may be suitable with parameter changes
#these locations can be found in the game mechanics doc
checkpointList = []
startCheckpoint = TownCheckpoint(20,"Start")
checkpointList.append(startCheckpoint)

riverCheckpoint1 = RiverCheckpoint(20,"River 1")
checkpointList.append(riverCheckpoint1)

townCheckpoint1 = TownCheckpoint(20,"Python Junction")
checkpointList.append(townCheckpoint1)

riverCheckpoint2 = RiverCheckpoint(20,"River 2")
checkpointList.append(riverCheckpoint2)

townCheckpoint2 = TownCheckpoint(20,"Bear City")
checkpointList.append(townCheckpoint2)

riverCheckpoint3 = RiverCheckpoint(20,"River 3")
checkpointList.append(riverCheckpoint3)

townCheckpoint3 = TownCheckpoint(20,"Gold Creek")
checkpointList.append(townCheckpoint3)

riverCheckpoint4 = RiverCheckpoint(20,"River 4")
checkpointList.append(riverCheckpoint4)

finishCheckpoint = TownCheckpoint(0,"Finish")
checkpointList.append(finishCheckpoint)

player = Player("Farmer",800, 100, 0.7, 0, 100)
notARealGui = ""
scenarioManager = ScenarioManager(notARealGui,player)

checkpointManagerInstance = CheckpointManager(checkpointList,scenarioManager,player)


#tests
#should be Start town,
print(checkpointManagerInstance.currentCheckpoint.name)
#should be 20:
print("distNext 1:",player.distNext)
# creates a terminal menu for the town, only choice 1 (travel)will do anything right now
checkpointManagerInstance.townScenario(-1)
print("distNext 2:",player.distNext)
#if you choose choice 1 in the town scenario, this will advance you again and bring you to a river scenario. you can choose to ferry right then and it iwll spend the money
print("calling nextCheckpoint()")
checkpointManagerInstance.nextCheckpoint()
#should be 20, loops over into the new river checkpoint 
print("distNext 3:" ,player.distNext)
print(checkpointManagerInstance.currentCheckpoint.name)
#should be 650 since the player is a farmer
print("player money:",player.money)

#print a river choices text interface


#this simulates a river scenario called from the GUI - will simply the ferry scenario


    