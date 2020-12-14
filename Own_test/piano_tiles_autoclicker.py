import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# to_check=[625,525,425,325]
# done

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(625,500)[0] == 0:
        click(625,510)
    elif pyautogui.pixel(525,500)[0] == 0:
        click(525,510)
    elif pyautogui.pixel(425,500)[0] == 0:
        click(425,510)
    elif pyautogui.pixel(325,500)[0] == 0:
        click(325,510)