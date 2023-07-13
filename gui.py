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
        global image, image_tk

        # Colors used in the program
        self.bg = "#242734" #primary background color
        self.bgSecondary = "#333646" #secondary background color
        self.accentColor = "#54b3d6" #accent color

        self.title("The Oregon Trail with Python(s)")
        self.configure(bg=self.bg)

        # Load the image
        image = PIL.Image.open("Images/landscape/01.jpg")

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
        text_label = tk.Label(text_section, text="Your Text", fg="white", bg=self.bgSecondary)
        text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        button1 = tk.Button(buttons_frame, text="Play the Oregon Trail!", bg=self.accentColor,command=self.showPlayerSelectScreen)        

        self.styleButtons(button1, self.accentColor, self.bg)

        button1.pack(side="left", fill="both", expand=True)

        self.attributes("-fullscreen", True)
    
     # this function applys a style to the buttons
    def styleButtons(self, button, colorOnHover, colorOnLeave):

        button.config(width = 20, bg=colorOnLeave, fg="white", bd=0, font=("bold"), highlightthickness=1, highlightcolor="white", highlightbackground="white")

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))
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