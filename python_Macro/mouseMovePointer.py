import pyautogui as pag
import time
pag.moveTo(500, 500)

while True:
    pag.moveRel(500, 0)
    time.sleep(10)
    pag.moveRel(-500, 0)
