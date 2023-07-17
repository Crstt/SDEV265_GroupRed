import random
import csv

#from . import checkpointManager

class Player:
    def __init__(self, character:str, money:int, food:int, huntAdjust:int, buyAudjust:int, distNext:int):
        self.character = character
        self.money = money
        self.food = food
        self.huntAdjust = huntAdjust
        self.buyAdjust = buyAudjust
        self.distNext = distNext

def selectCharacter(chioce):
    filename = "characters.csv"
    options = {}
    
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            options[row[0]] = Player(*row[1:])

    return options[chioce].character, int(options[chioce].money), int(options[chioce].food), int(options[chioce].huntAdjust), int(options[chioce].buyAdjust), int(options[chioce].distNext)

def selectCharacterCMD():
    filename = "characters.csv"
    choices = {}
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            choices[row[0]] = Player(*row[1:])
    
    cKey = [*choices]
    c=0
    i= 0
    button2Label = "See Next Option"
    while c == 0:
        loopBoundry = len(choices)
        if i == loopBoundry:
            i=0
        #create character description for display
        hunt = str(float(choices[cKey[i]].huntAdjust))
        buy = str(float(choices[cKey[i]].buyAdjust))
        descriptionLabel = "The" + choices[cKey[i]].character + " starts with $" + choices[cKey[i]].money + ", and a " + hunt + " percent change to hunting as well as " + buy  +" percent change to buying costs."
        button1Label = "Choose " + choices[cKey[i]].character
        """
        This will need to be editied to configure to the GUI button clicks beyond this point. This is essentially a sample of what the code should sortof look like
        The input and if statements are for testing purposes only
        button1.click()
            c=i
        button2.click()
            i+=1
        """
        print(descriptionLabel)
        print(button1Label)
        print(button2Label)

        selection = input("what button do you click? b1 - b2  ")
        if selection == "b1":
            c=i
            return choices[cKey[c]].character, int(choices[cKey[c]].money), int(choices[cKey[c]].food), int(choices[cKey[c]].huntAdjust), int(choices[cKey[c]].buyAdjust), int(choices[cKey[c]].distNext)
        else: i += 1

def generatePlayerChoices():
    filename = "characters.csv"
    choices = {}
    with open(filename, 'r') as csvfile:
        for row in csv.reader(csvfile):
            choices[row[0]] = Player(*row[1:])
    
    cKey = [*choices]
    return choices