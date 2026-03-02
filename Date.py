# Made by Sovf!

import time

Months = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

LocalTime = time.localtime()

print(LocalTime.tm_mday, Months[LocalTime.tm_mon], LocalTime.tm_year, (str(LocalTime.tm_hour) + ":" + str(LocalTime.tm_min) + ":" + str(LocalTime.tm_sec)))
