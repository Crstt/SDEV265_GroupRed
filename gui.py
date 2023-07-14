from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import PIL as PIL
from PIL import Image, ImageTk 

from player import *
from scenarioManager import *
from checkpointManager import CheckpointManager,createCheckpointList
from checkpoints.checkpoint import *

class StartGui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Colors used in the program
        self.bg = "#242734" #primary background color
        self.bgSecondary = "#333646" #secondary background color
        self.accentColor = "#54b3d6" #accent color
        self.defineGui()
        
    
    def defineGui(self):
        
        global image_tk

        self.title("The Oregon Trail with Python(s)")
        self.configure(bg=self.bg)

        # Load the image
        image = self.resizeImage(Image.open("Images/landscape/01.jpg"))

        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Configure the grid row and column weights to control the vertical and horizontal resizing
        self.grid_rowconfigure(0, weight=5)  # 50% vertical space
        self.grid_rowconfigure(1, weight=2)  # 20% vertical space
        self.grid_rowconfigure(2, weight=3)  # 30% vertical space
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, text="Your Text", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        button1 = tk.Button(buttons_frame, text="Play the Oregon Trail!", bg=self.accentColor,command=self.showPlayerSelectScreen)        

        self.styleButtons(button1, self.accentColor, self.bg)

        button1.pack(side="left", fill="both", expand=True)

        self.attributes("-fullscreen", True)

    def mainLogic(self):
        #implement instance of player
        self.player = Player(*selectCharacter())

        # create a scenarioManager instance
        self.scenarioManager = ScenarioManager(self, self.player)

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

        self.checkpointManager = CheckpointManager(checkpointList, self.scenarioManager, self.player)
        self.checkpointManager.nextScenario()
    
    # this function applys a style to the buttons
    def styleButtons(self, button, colorOnHover, colorOnLeave):

        button.config(width = 20, bg=colorOnLeave, fg="white", bd=0, font=("bold"), highlightthickness=1, highlightcolor="white", highlightbackground="white")

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

    def resizeImage(self, image):
        # Calculate the aspect ratio to maintain the image's proportions
        aspect_ratio = image.width / image.height

        # Calculate the width and height based on the desired proportions
        width = self.winfo_screenwidth()
        height = int(self.winfo_screenheight() * 0.5)  # 50% vertical space

        # Resize the image while preserving the aspect ratio
        image = image.resize((int(height * aspect_ratio), height))

        return image
    
    def updateImage(self, imageName):
        global image_tk
        
        if os.path.exists(f"scenarios/Scenario{imageName}/01.jpg"):
            image = self.resizeImage(Image.open(f"scenarios/Scenario{imageName}/01.jpg"))
            image_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_tk)
        else:
            print("Image not found")

    # Function that allows to update main window with the option of two buttons and a description
    def scenarioWindow(self,scenario):
        scenarioName = scenario.name 
        scenarioDescription = scenario.description

        self.updateImage(scenarioName)
        self.text_label.config(text=scenarioDescription)     

        # If the scenario has two choices, the second button is enabled
        if scenario.choices != []:
            self.button1.config(text=scenario.choices[0], command=lambda: self.scenarioManager.guiCallScenario(scenario, 1))
            self.button2.config(text=scenario.choices[1], command=lambda: self.scenarioManager.guiCallScenario(scenario, 2))
            self.button2.config(state="normal")

        else:
            self.button1.config(text="Continue", command=lambda: self.scenarioManager.guiCallScenario(scenario))
            self.button2.config(text="", command='')
            self.button2.config(state="disabled")
        
        self.update()
        self.update_idletasks()

    # Function that allows to updates the window with the result of the scenario
    def scenarioOutput(self, mod):
        self.text_label.config(text=mod.result)
        if mod.death == True:
            self.button1.config(text="Continue", command=lambda: messagebox.showinfo("DEVELOP GAME OVER LOGIC", "DEVELOP GAME OVER LOGIC"))
        else:
            self.button1.config(text="Continue", command=lambda: self.checkpointManager.nextScenario())
            
        self.button2.config(text="", command='')
        self.button2.config(state="disabled")

    def showTownCheckpoint(self,checkpoint):
        global image, image_tk
        #takes a town checkpoint and makes a window with the options
        deleteVar = 1
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = PIL.Image.open(self.checkpointManagerInstance.currentCheckpoint.imgPath)
        # Calculate the aspect ratio to maintain the image's proportions
        aspect_ratio = image.width / image.height
        # Calculate the width and height based on the desired proportions
        width = self.winfo_screenwidth()
        height = int(self.winfo_screenheight() * 0.5)  # 50% vertical space
        # Resize the image while preserving the aspect ratio
        image = image.resize((int(height * aspect_ratio), height))
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        image_label = tk.Label(self, image=image_tk, bg=self.bg)
        image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        text_label = tk.Label(text_section, text=f"You are at {self.checkpointManagerInstance.currentCheckpoint.name}.What would you like to do?", fg="white", bg=self.bgSecondary)
        text_label.pack(fill="both", expand=True)

        #player choice selection   
        #load the player choices
        playerChoices=generatePlayerChoices()
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        #Travel on button
        button1 = tk.Button(buttons_frame, text="Travel onwards", bg=self.accentColor, command=lambda: self.checkpointManagerInstance.townScenario(1))       
        button1.pack(side="left", fill="both", expand=True) 
        button2 = tk.Button(buttons_frame, text="Buy supplies", bg=self.accentColor, command=lambda: self.checkpointManagerInstance.townScenario(2))       
        button2.pack(side="left", fill="both", expand=True) 
        #Buy supplies button
        #3rd option button
        

    #allows you to select a player type
    def showPlayerSelectScreen(self):
        global image, image_tk
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = PIL.Image.open("Images/characterSelection/03.jpg")
        # Calculate the aspect ratio to maintain the image's proportions
        aspect_ratio = image.width / image.height
        # Calculate the width and height based on the desired proportions
        width = self.winfo_screenwidth()
        height = int(self.winfo_screenheight() * 0.5)  # 50% vertical space
        # Resize the image while preserving the aspect ratio
        image = image.resize((int(height * aspect_ratio), height))
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        image_label = tk.Label(self, image=image_tk, bg=self.bg)
        image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        text_label = tk.Label(text_section, text="What is your background? Bankers have 2000$, Merchants 1500$, and Farmers 1000$. However, farmers are the most skilled at surviving off the land, and Bankers are the least skilled. ", fg="white", bg=self.bgSecondary)
        text_label.pack(fill="both", expand=True)

        #player choice selection   
        #load the player choices
        playerChoices=generatePlayerChoices()
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        for choice in playerChoices:
            # generate a new button
            button1 = tk.Button(buttons_frame, text=playerChoices[choice].character, bg=self.accentColor, command=lambda choice=choice: self.createScenarioManager(playerChoices[choice]))       
            button1.pack(side="left", fill="both", expand=True) 

    def createScenarioManager(self,playerChoice):
        self.scenarioManager = ScenarioManager(self,playerChoice)
        self.checkpointManagerInstance = CheckpointManager(createCheckpointList(),self.scenarioManager,playerChoice)
        
        self.showTownCheckpoint(self.checkpointManagerInstance.currentCheckpoint)