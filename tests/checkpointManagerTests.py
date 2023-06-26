from checkpointManager import *
from checkpoints.town import *
from checkpoints.river import *

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

scenarios={"river"}
scenarioManager = ScenarioManager(scenarios)
checkpointManagerInstance = CheckpointManager(checkpointList,ScenarioManager)

#tests
#should be Start
print(checkpointManagerInstance.currentCheckpoint.name)
#creates text based interface for manipulating a town. calls the scenarios, but doesn't actually do anything
#scenario manager will print the scenario name
checkpointManagerInstance.townScenario(-1)

#update state then print the new checkpoint, should print "River 1"
checkpointManagerInstance.updateState()
print(checkpointManagerInstance.currentCheckpoint.name)

#print a river choices text interface
checkpointManagerInstance.riverScenario(-1)

#this simulates a river scenario called from the GUI - will simply call a scenario
checkpointManagerInstance.riverScenario(2)

#progress through all the remaining checkpoints to trigger a gameover
for x in range(0,7):
    checkpointManagerInstance.updateState()
    