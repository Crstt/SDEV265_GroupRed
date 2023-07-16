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
    def __init__(self, debug=False):
        super().__init__()

        # Colors used in the program
        self.bg = "#242734" # primary background color (dark blueish-black)
        self.bgSecondary = "#333646" # secondary background color (dark grayish-blue)
        self.accentColor = "#A87950" # accent color (light blue)
        self.textColor = "#ffffff" # text color (white)
        self.debug = debug
        self.defineGui()
        
    
    def defineGui(self):        
        global image_tk

        self.title("The Oregon Trail with Python(s)")
        self.configure(bg=self.bg)
        # Load the image
        image = self.resizeImage(PIL.Image.open("Images/landscape/01.jpg"))
        
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
        self.text_label = tk.Label(text_section, font=("Arial", 22), text="Your Text", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        self.button1 = tk.Button(buttons_frame, text="Play the Oregon Trail!", bg=self.accentColor,command=self.showPlayerSelectScreen)        

        self.styleButtons(self.button1, self.accentColor, self.bg)

        self.button1.pack(side="left", fill="both", expand=True)

        self.attributes("-fullscreen", True)       

    def defineScenarioGui(self):
        global image_tk

        # Load the image
        if os.path.exists("Images/landscape/01.jpg"):
            image = self.resizeImage(PIL.Image.open("Images/landscape/01.jpg"))
            image_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_tk)
        else:
            print("Image not found")

        
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
        self.text_label = tk.Label(text_section, font=("Arial", 22), text="Your Text", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        self.button1 = tk.Button(buttons_frame, text="Button 1", bg=self.accentColor, command=lambda: messagebox.showinfo("Test", "Pressed button 1"))        
        self.button2 = tk.Button(buttons_frame, text="Button 2", bg=self.accentColor, command=lambda: messagebox.showinfo("Test", "Pressed button 2"))

        self.styleButtons(self.button1, self.accentColor, self.bg)
        self.styleButtons(self.button2, self.accentColor, self.bg)

        self.button1.pack(side="left", fill="both", expand=True)
        self.button2.pack(side="left", fill="both", expand=True)
    
    #function that increases the font size of a tkinter item passed
    def increaseFontSize(self, item, amount):
        current_font = item['font']
        font_size = int(current_font['size'])
        new_font = (current_font['family'], font_size + amount)
        item.config(font=new_font)
    
    # this function applys a style to the buttons
    def styleButtons(self, button, colorOnHover, colorOnLeave):

        button.config(width = 20, bg=colorOnLeave, fg="white", bd=0, font=("Arial", 20), highlightthickness=1, highlightcolor="white", highlightbackground="white")

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
        height = int(self.winfo_screenheight() * 0.6)  # 50% vertical space

        # Resize the image while preserving the aspect ratio
        image = image.resize((int(height * aspect_ratio), height))

        return image
    
    def updateImage(self, imageName):
        global image_tk
        
        if os.path.exists(f"scenarios/Scenario{imageName}/01.jpg"):
            image = self.resizeImage(PIL.Image.open(f"scenarios/Scenario{imageName}/01.jpg"))
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
            self.button1.config(text="GAME OVER", command=lambda: self.showDeathScreen())
        elif mod.sick:
            self.button1.config(text="Continue", command=lambda: self.scenarioManager.callScenarioByName('Sickness'))
        else:
            self.button1.config(text="Continue", command=lambda: self.checkpointManager.nextScenario())
            
        self.button2.config(text="", command='')
        self.button2.config(state="disabled")

    def showTownCheckpoint(self,checkpoint):
        global image_tk
        #takes a town checkpoint and makes a window with the options
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()

        #characters image
        #Load the image
        image =PIL.Image.open(self.checkpointManager.currentCheckpoint.imgPath)
        
        image = self.resizeImage(image)
        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, font=("Arial", 22), text=f"You are at {self.checkpointManager.currentCheckpoint.name}.\nYou have {self.player.food} pounds of food, and {self.player.money} dollars. \nWhat would you like to do?", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        #player choice selection   
        #load the player choices
        playerChoices=generatePlayerChoices()
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        #Travel on button
        self.button1 = tk.Button(buttons_frame, text="Travel onwards", bg=self.accentColor, command=lambda: self.checkpointManager.townScenario(1))     
        self.styleButtons(self.button1, self.accentColor, self.bg)  
        self.button1.pack(side="left", fill="both", expand=True) 
        
        self.button2 = tk.Button(buttons_frame, text="Buy supplies", bg=self.accentColor, command=lambda: self.buyFoodScreen())       
        self.styleButtons(self.button2, self.accentColor, self.bg)
        self.button2.pack(side="left", fill="both", expand=True) 
        #Buy supplies button
        #3rd option button
        
    #allows you to select a player type
    def showPlayerSelectScreen(self):
        global image_tk
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = self.resizeImage(PIL.Image.open("Images/characterSelection/03.jpg"))
        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, font=("Arial", 22), text="What is your background? Bankers have 2000$, Merchants 1500$, and Farmers 1000$.\nHowever, farmers are the most skilled at surviving off the land, and Bankers are the least skilled. ", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        #player choice selection   
        #load the player choices
        playerChoices=generatePlayerChoices()
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        buttons = []
        i = 0
        for choice in playerChoices:
            # generate a new button            
            buttons.append(tk.Button(buttons_frame, text=playerChoices[choice].character, bg=self.accentColor, command=lambda choice=choice: self.initPlayer(choice)))
            self.styleButtons(buttons[-1], self.accentColor, self.bg)
            buttons[-1].pack(side="left", fill="both", expand=True)
            i += 1

    def initPlayer(self, choice):
        self.player = Player(*selectCharacter(choice))
        self.scenarioManager = ScenarioManager(self, self.player)
        checkpointList = createCheckpointList()

        self.checkpointManager = CheckpointManager(checkpointList, self.scenarioManager, self.player,self)
        self.defineScenarioGui()
        if not self.debug:
            self.checkpointManager.nextScenario()

    #Functio that shows the end screen for sucessful completion
    def showEndScreen(self):
        global image_tk
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = self.resizeImage(PIL.Image.open("Images/win/01.jpg"))
        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, font=("Arial", 22), text="Congratulations! You have made it to the end of the trail!", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        self.button1 = tk.Button(buttons_frame, text="Quit", bg=self.accentColor,command=lambda: self.quit())        

        self.styleButtons(self.button1, self.accentColor, self.bg)

        self.button1.pack(side="left", fill="both", expand=True)

    #Function that shows the end screen for when the player dies
    def showDeathScreen(self):
        global image_tk
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = self.resizeImage(PIL.Image.open("Images/death/01.jpg"))
        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, font=("Arial", 22), text="You have died! Better luck next time!", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        # Create a frame for the buttons below the text section
        buttons_frame = tk.Frame(self, bg=self.bgSecondary)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Create the buttons inside the frame
        self.button1 = tk.Button(buttons_frame, text="Quit", bg=self.accentColor,command=lambda: self.quit())        

        self.styleButtons(self.button1, self.accentColor, self.bg)

        self.button1.pack(side="left", fill="both", expand=True)
    
    def buyFoodScreen(self):
        global image_tk
        #clear the gui
        for ele in self.winfo_children():
            ele.destroy()
        #characters image
        #Load the image
        image = self.resizeImage(PIL.Image.open("Images/characterSelection/03.jpg"))
        
        # Convert the image to Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.image_label = tk.Label(self, image=image_tk, bg=self.bg)
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        #prompt text
        # Create a text section below the image
        text_section = tk.Frame(self, bg=self.bgSecondary)
        text_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Create a label inside the text section to display the text
        self.text_label = tk.Label(text_section, font=("Arial", 22), text=f"How much food would you like to buy? 1 Pound is {self.checkpointManager.currentCheckpoint.foodCost}$.", fg="white", bg=self.bgSecondary)
        self.text_label.pack(fill="both", expand=True)

        #create the text entry field
        textField = tk.Entry(self)
        textField.grid(row=2, column=0, columnspan=2, sticky="nsew")

        #create a button to confirm and buy the food
        purchaseButton = tk.Button(self,text="Purchase", bg=self.accentColor, command=lambda: purchaseFood(self,textField))
        purchaseButton.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(0, weight=4)  # 50% vertical space
        self.grid_rowconfigure(1, weight=2)  # 20% vertical space
        self.grid_rowconfigure(2, weight=2)  # 30% vertical space
        self.grid_rowconfigure(2, weight=2)  # 30% vertical space
def purchaseFood(self,textField):
    
    amount = int(textField.get())
    if(self.player.money>=amount*self.checkpointManager.currentCheckpoint.foodCost):
        self.player.food += amount
        self.player.money -=amount*self.checkpointManager.currentCheckpoint.foodCost
    self.showTownCheckpoint(self.checkpointManager.currentCheckpoint)
    