'''import calendar

for i in range (12) :
    cal = calendar.month (2023, i + 1)
    print()
    print (cal)'''
    
import calendar

year = int(input("year? : "))
month = int(input("month? : "))

print (calendar.month (year, month))