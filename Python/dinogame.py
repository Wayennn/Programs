import pyautogui as pag
import time

#time.sleep(2)
print(pag.position())

check_color = (172, 172, 172)

def up(dt):
    pag.keyDown("up")
    time.sleep(dt)
    pag.keyUp("up")
def down(dt):
    pag.keyDown("down")
    time.sleep(dt)
    pag.keyUp("down")

x = 237
i = 0
dt = 2.0
while True:
    t = time.perf_counter()
    if (not pag.pixelMatchesColor(x, 449, check_color)) and pag.pixelMatchesColor(x, 389, check_color):
        down(dt)
    elif pag.pixelMatchesColor(x, 449, check_color):
        up(dt)
    if i%10000000==0:
        x += 1
        if dt>0.5:
            dt -= 0.1
    print(time.perf_counter()-t)