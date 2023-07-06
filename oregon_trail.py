from scenarioManager import *
import player
from player import *
import checkpointManager
import gui

# create a gui instance
root = gui.StartGui()

# create a scenarioManager instance
scenarioManager = ScenarioManager(root)

#starts the gui main loop
root.mainloop()

#implement instance of player
player1 = Player(*selectCharacter())

