def checkLeapYear(year):
#importing the calendar module
    import calendar

    return(calendar.isleap(year))
year = int(input("Enter the year: "))
if (checkLeapYear(year)):

    print("Leap Year")
else:

    print("Not a Leap Year")