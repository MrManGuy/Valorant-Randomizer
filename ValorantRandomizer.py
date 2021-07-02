import pyautogui as pygui
from tkinter import *
from tkinter import messagebox, ttk
import sys, time, random, math

#Config
delayAfterActivation = 3
unassignedPNG = 'Unassigned.PNG'

#Tkinter
window = Tk()

window.title("Valorant Randomizer")
tab_control = ttk.Notebook(window)
home = ttk.Frame(tab_control)
agents = ttk.Frame(tab_control)
skins = ttk.Frame(tab_control)
tab_control.add(home, text="Home")
tab_control.add(agents, text="Agents")
tab_control.add(skins, text="Skins")
tab_control.grid(column=0, row=0, columnspan=4, sticky="W")
#Valorant locations of everything (1920x1080)
locations = {
    "skins": {
        'Classic': (450, 250),
        "Stinger":(750, 250),
        "Bulldog": (1150, 250),
        "Marshal": (1550, 250),
        "Shorty": (450, 400),
        "Spectre": (750, 400),
        "Guardian": (1150, 400),
        "Operator": (1550, 400),
        "Frenzy": (450, 600),
        "Bucky": (750, 600),
        "Phantom": (1150, 600),
        "Ares": (1550, 600), 
        "Ghost": (450, 750),
        "Judge": (750, 750),
        "Vandal": (1150, 750),
        "Odin": (1550, 750),
        "Sheriff": (500, 900),
        "Knife": (1550, 900),
    },
    "sprays": {
        "Preround-Spray": (1505, 725),
        "Midround-Spray": (1605, 725),
        "Postround-Spray": (1695, 725),
    },
    "cards":{
        "Card": (230, 410)
    },
    "agents": {
        "Breach": (710, 920),
        "Brimstone": (790, 920),
        "Cyper": (875, 920),
        "Jett": (960, 920),
        "Killjoy": (1045, 920),
        "Omen": (1125, 920),
        "Phoenix": (1210, 920),
        "Raze": (710, 1000),
        "Reyna": (790, 1000),
        "Sage": (875, 1000),
        "Skye": (960, 1000),
        "Sova": (1045, 1000),
        "Viper": (1125, 1000),
        "Yoru": (1210, 1000),
    }
}

checks = {
    "skins": {
        'Classic': IntVar(),
        "Stinger": IntVar(),
        "Bulldog": IntVar(),
        "Marshal": IntVar(),
        "Shorty":  IntVar(),
        "Spectre": IntVar(),
        "Guardian": IntVar(),
        "Operator": IntVar(),
        "Frenzy": IntVar(),
        "Bucky": IntVar(),
        "Phantom": IntVar(),
        "Ares": IntVar(), 
        "Ghost": IntVar(),
        "Judge": IntVar(),
        "Vandal": IntVar(),
        "Odin": IntVar(),
        "Sheriff": IntVar(),
        "Knife": IntVar(),
        "Preround-Spray": IntVar(),
        "Midround-Spray": IntVar(),
        "Postround-Spray": IntVar(),
        "Card": IntVar(),
        "Title": IntVar(),
        "Buddies?": IntVar()
    },
    "agents": {
        "Astra": IntVar(),
        "Breach": IntVar(),
        "Brimstone": IntVar(),
        "Cypher": IntVar(),
        "Jett": IntVar(),
        "KayO": IntVar(),
        "Killjoy": IntVar(),
        "Omen": IntVar(),
        "Phoenix": IntVar(),
        "Raze": IntVar(),
        "Reyna": IntVar(),
        "Sage": IntVar(),
        "Skye": IntVar(),
        "Sova": IntVar(),
        "Viper": IntVar(),
        "Yoru": IntVar(),
    }
}
#Helper function to iterate through weapon skins, cards, and sprays
def rotateThrough(direction):
    for i in range(0, random.randrange(int(min_rotations.get()), int(max_rotations.get()))):
        pygui.press(direction)
        time.sleep(0.01)
#Function to randomly select an agent on the agent selection screen
def randomizeAgent():
    agentSelection = []
    for agent in checks['agents'].keys():
        if pygui.locateOnScreen("imgs/" + agent.lower() + ".png", confidence=0.9) != None:
            print("Found", agent)
        if checks['agents'][agent].get() == 1:
            agentSelection.append(agent)
    a = random.choice(agentSelection)
    lbl_agent.config(text = a) 
    time.sleep(delayAfterActivation)
    pygui.moveTo(x=locations['agents'][a][0], y=locations['agents'][a][1], duration=0.15)
    pygui.click()
    time.sleep(0.5)
    pygui.moveTo(x=950, y=810, duration=0.15)
    pygui.click()
#Helper function to randomly select skins for each gun
def randomizeWeapons():
    time.sleep(delayAfterActivation)
    for location in locations["skins"]:
        if checks['skins'][location].get() != 0:
            coord = locations['skins'][location]
            pygui.moveTo(x=1300, y=25, duration=0.15)
            pygui.click()
            pygui.moveTo(x=coord[0], y=coord[1], duration=0.15)
            pygui.click()
            time.sleep(0.1)
            rotateThrough("right")
            time.sleep(0.1)
            pygui.moveTo(x=1600, y=820, duration=0.15)
            pygui.click()
            time.sleep(0.1)
            if(checks['skins']['Buddies?'].get() == 1):
                pygui.moveTo(x=1015, y=193, duration=0.15)
                pygui.click()
                while True:
                    time.sleep(0.1)
                    rotateThrough("right")
                    time.sleep(0.1)
                    if pygui.locateOnScreen("imgs/" + unassignedPNG, grayscale=True, confidence=0.9) != None:
                        break
                pygui.moveTo(x=1600, y=820, duration=0.15)
                pygui.click()
                time.sleep(0.1)
            pygui.press('esc')
            time.sleep(0.05)
#Helper function to randomly select sprays for each category
def randomizeSprays():
    time.sleep(delayAfterActivation)
    for location in locations["sprays"]:
        if checks['skins'][location].get() != 0:
            coord = locations['sprays'][location]
            pygui.moveTo(x=1300, y=25, duration=0.15)
            pygui.click()
            time.sleep(0.05)
            pygui.moveTo(x=230, y=735, duration=0.2)
            pygui.click()
            time.sleep(0.05)
            rotateThrough("right")
            time.sleep(0.05)
            pygui.moveTo(x=coord[0], y=coord[1], duration=0.15)
            pygui.click()
            time.sleep(0.05)
            pygui.moveTo(x=1600, y=820, duration=0.15)
            pygui.click()
            time.sleep(0.05)
            pygui.press('esc')
            time.sleep(0.05)
#Helper function to randomly select card
def randomizeCard():
    time.sleep(delayAfterActivation)
    for location in locations["cards"]:
        if checks['skins'][location].get() != 0:
            coord = locations['cards'][location]
            pygui.moveTo(x=1300, y=25, duration=0.15)
            pygui.click()
            time.sleep(0.1)
            pygui.moveTo(x=coord[0], y=coord[1], duration=0.15)
            pygui.click()
            time.sleep(0.1)
            rotateThrough("right")
            pygui.click()
            time.sleep(0.1)
            pygui.moveTo(x=1600, y=820, duration=0.15)
            pygui.click()
            time.sleep(0.1)
            pygui.press('esc')
            time.sleep(0.05)
#Function to randomize all skins
def randomizeAll():
    randomizeWeapons()
    randomizeSprays()
    randomizeCard()

pygui.PAUSE = 0.01

#Agents
lbl_agents = Label(agents, text="Select agents to choose from:", justify=LEFT)
lbl_agents.grid(column=0, row=0, columnspan=2, sticky = W)

checkBoxes = []
location = 2
for key in checks["agents"].keys():
    checkBoxes.append(Checkbutton(agents, text=key, variable=checks["agents"][key], onvalue=1, offvalue=0, justify=LEFT))
    checks["agents"][key].set(1)
    checkBoxes[-1].grid(row=math.floor(location/4),column=location%4, sticky = W)
    location = location + 1

lbl_agent_choice = Label(agents, text="Selection:", justify=LEFT)
lbl_agent_choice.grid(column=2, row=10,  sticky = W)

lbl_agent = Label(agents, text="NONE", justify=LEFT)
lbl_agent.grid(column=3, row=10,  sticky = W)

btn_agent_select = Button(agents, text="Randomly select agent", command=randomizeAgent)
btn_agent_select.grid(column=0, row=10, columnspan=2)

#Skins
lbl_min_rotations = Label(skins, text="Min Rotations:")
lbl_min_rotations.grid(column=0, row=1)

minRots = IntVar()
minRots.set(1)
min_rotations = Spinbox(skins, from_=0, to=500, width=10, textvariable=minRots)
min_rotations.grid(column=1, row=1)

lbl_max_rotations = Label(skins, text="Max Rotations:")
lbl_max_rotations.grid(column=2, row=1)

maxRots = IntVar()
maxRots.set(30)
max_rotations = Spinbox(skins, from_=0, to=500, width=10, textvariable=maxRots)
max_rotations.grid(column=3, row=1)

lbl_weapons = Label(skins, text="Select weapons to randomize:", justify=LEFT)
lbl_weapons.grid(column=0, row=2, columnspan=2, sticky = W)

lbl_sprays = Label(skins, text="Sprays to randomize:", justify=LEFT)
lbl_sprays.grid(column=0, row=7, columnspan=2, sticky = W)

lbl_titles = Label(skins, text="Extras to randomize:", justify=LEFT)
lbl_titles.grid(column=0, row=8, columnspan=2, sticky = W)

location = 10
for key in checks["skins"].keys():
    checkBoxes.append(Checkbutton(skins, text=key, variable=checks["skins"][key], onvalue=1, offvalue=0, justify=LEFT))
    checks["skins"][key].set(1) 
    if(location >= 28 and location < 31):
        checkBoxes[-1].grid(row=7,column=location-27, sticky = W)
    elif(location == 31):
        checkBoxes[-1].grid(row=8,column=2, sticky = W)
    elif(location == 32):
        checkBoxes[-1].grid(row=8,column=1, sticky = W)
        checks["skins"][key].set(0)
    elif(location == 33):
        checkBoxes[-1].grid(row=8,column=3, sticky = W)
    else:
        checkBoxes[-1].grid(row=math.floor(location/4),column=location%4, sticky = W)
    location = location + 1

btn_randomize = Button(skins, text="Randomize", command=randomizeAll)
btn_randomize.grid(row=9, column=1, columnspan=2, sticky="nsew")

window.mainloop()