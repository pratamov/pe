from datetime import datetime

year1, month1, date1 = 1900, 1, 1
year2, month2, date2 = 2000, 12, 31

day_of_week = 0
sundays = 0
while (year1*1000 + month1*100 + date1) < (year2*1000 + month2*100 + date2):
    if month1 in [1,3,5,7,8,10,12] and date1 > 30:
        date1 = 1
        if month1 == 12:
            month1 = 1
            year1 += 1
        else:
            month1 += 1
    elif month1 in [4,6,9,11] and date1 > 29:
        date1 = 1
        month1 += 1
    elif month1 == 2:
        if ((year1%4 == 0 and year1%100 >0) or (year1%400)) and date1 > 27:
            date1 = 1
            month1 += 1
        elif date1 > 28:
            date1 = 1
            month1 += 1
        else:
            date1 += 1
    else:
        date1 += 1

    day_of_week = (day_of_week + 1) % 7
    if year1*1000 + month1*100 + date1 >= (1901*1000 + 100 + 1) and day_of_week == 0 and date1 == 1:
        sundays += 1

print(sundays)
