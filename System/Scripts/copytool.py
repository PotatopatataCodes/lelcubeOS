import time
import pyperclip as clippy
import json
import os
import xml.dom.minidom
from xml.etree import ElementTree

# Boring XML stuff
document = xml.dom.minidom.parse("System/GlobalReplyDatabase.xml")
eattrees = ElementTree.parse("System/GlobalReplyDatabase.xml")
root = eattrees.getroot()

# Boring JSON stuff
with open("System/lelcubeOS.json", 'r') as f:
    lelcubeOS = json.load(f)

def process_input(str):
    ues = ""

    # db command gets the inner text of the element with the input the user gives
    if str.startswith("db "):
        dbkey = str.split(" ")[1]
        ues = root.find(dbkey).text
    
    # db but it finds stuff inside elements
    if str.startswith("dbi "):
        dbkey = str.split(" ")[1]
        yourmomuwu = str.split(" ")[2]
        Microsoft_Windows_XP = root.find(dbkey)
        hey_if_you_are_a_new_technologies_employee_and_you_are_reading_this_code_then_fu = Microsoft_Windows_XP.find(yourmomuwu)
        ues = hey_if_you_are_a_new_technologies_employee_and_you_are_reading_this_code_then_fu.text

    else:
        print("Command not found")
    
    return ues

# Dual-boot support
if lelcubeOS["hasFanOS"] == False:
    clippy.copy(process_input("db boot"))
else:
    # We have a clipboard so it's ok
    clippy.copy(process_input("db boot"))
    clippy.copy(process_input("db lelboot-fanos"))

time.sleep(3)

# TODO: Add user support
clippy.copy(process_input("db desktop"))

ok = lelcubeOS["version"]

print(f"2023 Lelcube Technologies\nlelcubeOS Copy Tool 0.7 on lelcubeOS {ok}\nLeaking the lelcubeOS 15 beta source code and/or binaries will result in you losing your job\n")
while True:
    epokinput = input("> ")
    if epokinput == "exit" or epokinput == "quit":
        break

    elif epokinput.startswith("fs"):
        thething = ":file_folder: **Lelfinder**\n\n"
        wot = []
        args = epokinput.split(" ")
        thething = thething + "/" + args[1] + "/\n\n"
        the = os.scandir(args[1])

        # make file list
        for i in the:
            name = i.name
            icon = ""

            # Folder
            if i.is_dir():
                icon = ":file_folder:"
            # App
            elif name.endswith(".exe") or name.endswith(".lelapp"):
                icon = ":package:"
            # Driver
            elif name.endswith(".drv"):
                icon = ":wrench:"
            # Language
            elif name.endswith(".lang"):
                icon = ":map:"
            # Icon set
            elif name.endswith(".icn"):
                icon = ":symbols:"
            # Theme
            elif name.endswith(".thm"):
                icon = ":art:"
            # C 2 source file
            elif name.endswith(".c2"):
                icon = ":regional_indicator_c:"
            # C 2 module file
            elif name.endswith(".mod"):
                icon = ":toolbox:"
            # Assembly source file
            elif name.endswith(".asm"):
                icon = ":a:"
            # FanOS app
            elif name.endswith(".app"):
                icon = ":regional_indicator_f:"
            # Audio file
            elif name.endswith(".mp3") or name.endswith(".ogg") or name.endswith(".wav"):
                icon = ":musical_note:"
            # Video file
            elif name.endswith(".mp4") or name.endswith(".mov") or name.endswith(".mpk"):
                icon = ":film_frames:"
            # Configuration file
            elif name.endswith(".json") or name.endswith(".xml"):
                icon = ":gear:"
            # TODO: Add support for more file formats
            else:
                icon = ":page_facing_up:"

            thething = f"{thething}> {icon} {i.name}\n"

        clippy.copy(thething)

    else:
        pain = process_input(epokinput)
        if not pain == "":
            clippy.copy(pain)
            print("copied")