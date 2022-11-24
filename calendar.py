# print calendar of any month of any year
import calendar

# input the year
year=int(input("Enter Year: "))

# input the month no.  (eg. 1 for january, 5 for may)
month=int(input("Enter Month:"))

# print the calendar
print(calendar.month(year,month))
