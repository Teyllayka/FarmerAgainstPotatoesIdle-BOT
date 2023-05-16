import cv2
import numpy as np
import pyautogui as pg


confidence1 = float(input('input confidence +- 0.85'))

while True:

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)

    potato2 = None
    while potato2 is None:
        potato2 = pg.locateOnScreen(
            'image2.png', grayscale=True, confidence=confidence1)
    pg.leftClick(potato2.width/2 + potato2.left,
                 potato2.height/2 + potato2.top)
