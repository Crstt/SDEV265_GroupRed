#This files acts as the main oregon_trail.py for test purposes 
import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory


import scenarioManager
import player
import checkpointManager
import gui

# create a gui instance
root = gui.StartGui()

# create a scenarioManager instance
scenarioManager = scenarioManager.ScenarioManager(root)
print(scenarioManager.scenarios)
print(scenarioManager.callRandomScenario())
print(scenarioManager.callRandomScenario())
print(scenarioManager.callRandomScenario())
print(scenarioManager.callRandomScenario())

#starts the gui main loop
root.mainloop()

#implement instance of player