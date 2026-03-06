#PRIYANSHU PABARI 590022242

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
# Days in each month
if month in [1,3,5,7,8,10,12]:
    max_days = 31
elif month in [4,6,9,11]:
    max_days = 30
elif month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year 
% 100 != 0):
        max_days = 29
    else:
        max_days = 28
        day += 1
if day > max_days:
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1
print("Next date is:")
print("day =", day, "month =", 
month, "year =", year)