import calendar
from math import fmod
from datetime import date, datetime

AGE = 29.530588853


def lunar_phases(day):

	lunar_views = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
	day_of_new = date(2000, 1, 6) 

	displacement_days = (day - day_of_new).days
	lunar_age = fmod(displacement_days, PERIOD)
	icon_index = int(lunar_age / (AGE / len(lunar_views)))

	return lunar_views[icon_index]
	

if __name__ == "__main__":
	year = int(input("Year > "))
	month = int(input("Month > "))
	
	lines = [date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]
	
	for line in lines:
	     print (f"{line.day} {lunar_phases(line)}", end="\t")
