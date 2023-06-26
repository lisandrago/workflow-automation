#Module 6 Assignment

#Question 1, revising the provided code for current date and time.
import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		current_time = datetime.now().strftime("%H:%M:%S")
		print("{0}\t{1}\t{2}".format(item, cost, current_time))

#Question 2, adding 1 day, 2 years, and subtracting 60 seconds
from datetime import datetime, timedelta

current_datetime = datetime.now()
one_day = current_datetime + timedelta(days=1)
two_years = current_datetime + timedelta(days=730)
last_minute = current_datetime + timedelta(seconds=-60)

print(one_day)
print(two_years)
print(last_minute,"\n")

#Question 3, using timedelta for 100 days, 10 hours, and 13 minutes
from datetime import timedelta
Final = timedelta(days = 100, hours = 10, minutes = 13)

print(Final)

#Question 4, writing a function that takes feet, inches, and time, got errors

	

