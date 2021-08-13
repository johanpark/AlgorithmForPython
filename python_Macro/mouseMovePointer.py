import pyautogui as pag
import time
pag.moveTo(500, 500)

while True:
    pag.moveRel(500, 0)
    time.sleep(5)
    pag.moveRel(-500, 0)
    pag.drag(300, 300, 3, button='left')
    pag.drag(300, 300, 3, button='right')