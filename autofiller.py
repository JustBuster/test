import pyautogui
import time
import winsound

clicksList = [[792, 583], [571, 830], [577, 780], [613, 1119]]
time.sleep(2)

for j in range(3):
    for i in clicksList:
        time.sleep(0.5)
        winsound.Beep(2500, 500)
        pyautogui.leftClick(i[0], i[1])
        time.sleep(1)
        pyautogui.scroll(-500)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "w")