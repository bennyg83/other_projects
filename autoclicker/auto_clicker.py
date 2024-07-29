import pyautogui
import keyboard
import threading
import time

clicking = False

def click_mouse():
    while clicking:
        for _ in range(100):
            pyautogui.click()
            time.sleep(0.01)  # small delay to make sure the system can handle the clicks

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        threading.Thread(target=click_mouse).start()

# Assigning the toggle function to the F8 key
keyboard.add_hotkey('F8', toggle_clicking)

print("Press F8 to toggle the clicking.")

# Keep the script running
keyboard.wait('esc')
