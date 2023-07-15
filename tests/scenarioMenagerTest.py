#This files acts as the main oregon_trail.py for test purposes 
import sys
import os
sys.path[0] = os.path.dirname(sys.path[0]) # Set path to the parent directory


import scenarioManager
import player
#import checkpointManager
import gui

# create a gui instance
root = gui.StartGui(debug=True)



def testSpecificScenarios():
    scenarioManager.callScenarioByName("Sickness")
    #if scenarioManager.callScenarioByName("River").death: return True
    #if scenarioManager.callScenarioByName("Fork").death: return True
    #if scenarioManager.callScenarioByName("Bison").death: return True


def testRandomScenarios(num):
    for i in range(1,num + 1):
        print(f"------------{i}------------")
        if scenarioManager.callRandomScenario().death: return True
        
input("Select a character in the gui, and press enter to start testing...")

scenarioManager = root.scenarioManager
if testSpecificScenarios(): quit()

#if testRandomScenarios(10): quit()



#starts the gui main loop
root.mainloop()

#implement instance of player