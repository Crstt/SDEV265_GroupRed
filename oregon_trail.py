from scenarioManager import *
import player
import checkpointManager
import gui

# create a gui instance
root = gui.StartGui()

# create a scenarioManager instance
scenarioManager = ScenarioManager(root)

#starts the gui main loop
root.mainloop()

#implement instance of player