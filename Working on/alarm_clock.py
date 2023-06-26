#alarm clock

from datetime import datetime, time, timedelta #i had to google how to do this part
import time

def set_alarm():
    alarm_time_input = input("please select a (military) time to set the alarm (HH:MM): ")
    alarm_time = datetime.strptime(alarm_time_input, "%H:%M").time()
    return alarm_time

while True:
    if datetime.time == set_alarm():
        print("Beep beep")

if __name__ == '__main__':
    main()