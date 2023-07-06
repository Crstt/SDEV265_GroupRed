from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

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
        image = Image.open("Images/landscape/01.jpg")

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
        button1 = tk.Button(buttons_frame, text="Button 1", bg=self.accentColor, command=lambda: messagebox.showinfo("Test", "Pressed button 1"))        
        button2 = tk.Button(buttons_frame, text="Button 2", bg=self.accentColor, command=lambda: messagebox.showinfo("Test", "Pressed button 2"))

        self.styleButtons(button1, self.accentColor, self.bg)
        self.styleButtons(button2, self.accentColor, self.bg)

        button1.pack(side="left", fill="both", expand=True)
        button2.pack(side="left", fill="both", expand=True)

        self.attributes("-fullscreen", True)
    
     # this function applys a style to the buttons
    def styleButtons(self, button, colorOnHover, colorOnLeave):

        button.config(width = 20, bg=colorOnLeave, fg="white", bd=0, font=("bold"), highlightthickness=1, highlightcolor="white", highlightbackground="white")

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))