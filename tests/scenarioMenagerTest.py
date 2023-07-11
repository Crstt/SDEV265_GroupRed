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
player = player.Player("Farmer",800, 100, 70, 0, 100)

# create a scenarioManager instance
scenarioManager = scenarioManager.ScenarioManager(root, player)

def testSpecificScenarios():
    if scenarioManager.callScenarioByName("Travel").death: return True
    #if scenarioManager.callScenarioByName("River").death: return True
    #if scenarioManager.callScenarioByName("Fork").death: return True
    #if scenarioManager.callScenarioByName("Bison").death: return True


def testRandomScenarios(num):
    for i in range(1,num + 1):
        print(f"------------{i}------------")
        if scenarioManager.callRandomScenario().death: return True
        
input("Press enter to start testing...")
if testSpecificScenarios(): quit()

#if testRandomScenarios(10): quit()



#starts the gui main loop
root.mainloop()

#implement instance of player