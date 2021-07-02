import os
import psutil
import pyautogui
from playsound import playsound

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged and percent >= 100:
    mp3 = f'{os.getcwd()}\\notification_sound.mp3'
    playsound(mp3)
    pyautogui.alert('Battery full, unplug charger!')
