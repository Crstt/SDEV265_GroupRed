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
    runAndPrint("Travelers")
    runAndPrint("Travelers")
    runAndPrint("Travelers")
    runAndPrint("Travelers")
    return True

def runAndPrint(scenarioName):
    scenarioManager.callScenarioByName(scenarioName)
    input("After running scenario in the GUI press enter to view results...")
    if scenarioName in scenarioManager.scenarios:
        mod = scenarioManager.scenarios[scenarioName].mod
        
    if scenarioName in scenarioManager.specialScenarios:
        mod = scenarioManager.specialScenarios[scenarioName].mod

    mod.printMods()
        
input("Select a character in the gui, and press enter to start testing...")

scenarioManager = root.scenarioManager
if testSpecificScenarios(): quit()



#starts the gui main loop
root.mainloop()

#implement instance of player