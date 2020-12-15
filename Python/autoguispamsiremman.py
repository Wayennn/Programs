import pyautogui as pag
import time
import csv

def enter_meeting():
    pag.click(282, 459) # at khub
    time.sleep(4)
    pag.hotkey("ctrl", "e")
    time.sleep(0.5)
    pag.hotkey("ctrl", "d")
    time.sleep(1)
    pag.click(992, 427) # join at meet
    time.sleep(2)

def start_record():
    pag.click(1338, 675) # three buttons
    time.sleep(0.5)
    pag.click(1210, 238) # record button
    time.sleep(0.5)
    pag.click(929, 483) # accept consent
    time.sleep(10)

def stop_record():
    pag.click(1338, 675) # three buttons
    time.sleep(1)
    pag.click(1210, 238) # record button
    time.sleep(1)
    pag.click(797, 466) # stop recording
    time.sleep(1)

def leave_meeting():
    pag.click(682, 685) # accept send to sir emman
    time.sleep(1)
    pag.hotkey("ctrl", "w")
    time.sleep(1)

def chat(_names):
    pag.click(1127, 89) # click chat
    time.sleep(1)
    for i in range(2, 48):
        pag.write("Magandang buhay!")
        pag.hotkey("shift", "enter")
        pag.write(_names[i])
        time.sleep(0.1)
        pag.press("enter")
        time.sleep(0.1)
    pag.click(1337, 102) # close chat
    time.sleep(1)

with open("Files/p6.csv") as sfile:
    cread = csv.reader(sfile, delimiter=",")
    names = [row[1] for row in cread]

time.sleep(1)
print(pag.position())

for i in range(1):
    enter_meeting()
    start_record()
    chat(names)
    stop_record()
    leave_meeting()
