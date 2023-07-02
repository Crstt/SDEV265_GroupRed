#This files acts as the main oregon_trail.py for test purposes 
import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory


import scenarioManager
import player
#import checkpointManager
import gui

# create a gui instance
root = gui.StartGui()

# create a player instance
player = player.Player("Farmer",800, 100, 1, 0, 100)

# create a scenarioManager instance
scenarioManager = scenarioManager.ScenarioManager(root, player)
#print(scenarioManager.scenarios)
print(scenarioManager.callScenarioByName("Fork"))
print(scenarioManager.callScenarioByName("Fork"))
print(scenarioManager.callScenarioByName("Travel"))
print(scenarioManager.callScenarioByName("Bison"))
print(scenarioManager.callScenarioByName("Fork"))
print(scenarioManager.callScenarioByName("Hunt"))

#starts the gui main loop
root.mainloop()

#implement instance of player