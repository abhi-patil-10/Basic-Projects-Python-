import time
from plyer import notification

while True:
    # build in module for notifications in windows
    notification.notify(title="Reminder",message="Drink a sip of water.....")
    
    time.sleep(5)