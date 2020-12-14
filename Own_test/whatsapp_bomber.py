import pyautogui
import time

# time to switch tabs
time.sleep(4)

# reading the file and then typing whatever we want to send them.
# remeber to select the textbox in the first 10 seconds
with open("send_data.txt", "r") as data:
    x = data.read()

# we can do this manually as well!
# x = "Good morning!"
for i in range(100):
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    time.sleep(0.2)