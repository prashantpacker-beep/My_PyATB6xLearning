#checking for leap year 2024--Yes
# Leap year occur in each year that is multiple od 4
# except for year evenly divisible by 100 but not 400
#the year is multiple of 400
#the year is multiple of 4 but not multiple of 100


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year=2024
#year=2026
result = check_leap_year(year)
print(result)


