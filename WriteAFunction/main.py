def is_leap(year):
    leap = False
    divByFour = year % 4
    divByHundred = year % 100
    divByFourHundred = year % 400
    leap = (divByFour == 0 and divByHundred != 0) or (divByFourHundred == 0)
    return leap

year = int(input())
print(is_leap(year))