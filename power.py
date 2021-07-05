import psutil
from pyautogui import alert

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged and percent >= 100:
    alert(
        text='Your Battery is Fully Charged, Please Unplug Your Charger!',
        title='BATTERY FULL NOTIFICATION',
        button='OK'
    )
