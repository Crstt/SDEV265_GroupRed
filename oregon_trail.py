from scenarioManager import *
import player
from player import *
import checkpointManager
import gui
from checkpoints.checkpoint import *



checkpointList = []
startCheckpoint = Checkpoint(False,20,"Start Place")
checkpointList.append(startCheckpoint)

riverCheckpoint1 = Checkpoint(True,20,"River 1")
checkpointList.append(riverCheckpoint1)

townCheckpoint1 = Checkpoint(False,20,"Python Junction")
checkpointList.append(townCheckpoint1)

riverCheckpoint2 = Checkpoint(True,20,"River 2")
checkpointList.append(riverCheckpoint2)

townCheckpoint2 = Checkpoint(False,20,"Bear City")
checkpointList.append(townCheckpoint2)

riverCheckpoint3 = Checkpoint(True,20,"River 3")
checkpointList.append(riverCheckpoint3)

townCheckpoint3 = Checkpoint(False,20,"Gold Creek")
checkpointList.append(townCheckpoint3)

riverCheckpoint4 = Checkpoint(True,20,"River 4")
checkpointList.append(riverCheckpoint4)

finishCheckpoint = Checkpoint(False,0,"Finish")
checkpointList.append(finishCheckpoint)

# create a gui instance
root = gui.StartGui()
#starts the gui main loop
root.mainloop()
playerChar = root.showPlayerSelectScreen()
print(playerChar.character)
# create a scenarioManager instance
scenarioManager = ScenarioManager(root,playerChar)



#implement instance of player
#player1 = Player(*selectCharacter())

