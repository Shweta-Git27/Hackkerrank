import pyautogui
import time

limit = input("Enter Limit:")
message = input("Enter message:")
i= 0
time.sleep(3)
while i < int(limit) :
    pyautogui.typewrite(message)
    
    pyautogui.press('enter')
    i = i +  1
    
