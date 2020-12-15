import pyautogui as pag
import time
import csv

scw, sch = pag.size()
print("Screen size (" + str(scw) + "," + str(sch) + ")")

cx, cy = pag.position()
print("Cursor position (" + str(cx) + "," + str(cy) + ")")

with open("Files/subjects.csv") as sfile:
    cread = csv.reader(sfile, delimiter = ",")
    rows = [row for row in cread]

time.sleep(2)

# pag.click(677, 708)
# pag.moveTo(100, 200, 2, pag.easeInOutEase)
# pag.moveTo(100, 200, 2, pag.easeInBounce)
# pag.moveTo(85, 100)
# pag.drag(100, 100, 0.5)

# for i in range(len(rows)):
#     pag.write(",".join(rows[i]))
#     pag.press("enter")
#
# for i in range(100):
#     bz = str(random.random())
#     pag.write(bz)
#     #pag.hotkey("shift", "enter")
#     #pag.write("Message number " + str(i+1))
#     pag.press("enter")
#     time.sleep(0.1)
nm = ["Maria", "Charisma", "Patambang", "Estrella"]
for i in range(100):
    pag.write("HELLO")
    pag.hotkey("shift", "enter")
    pag.write("My dear " + nm[i%4] + ". T = -" + str(100-i))
    time.sleep(0.5)
    pag.press("enter")
    time.sleep(1)
