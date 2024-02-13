import datetime

DAYS=("Monday","Tuesday"," Wednesday","Thursday","Friday","Saturday")
MONTHS=("January","February","March","April","May","June","July","August","September","October","November","December")
print("Calendar by @BandamaN")

while True:
    print('Enter the year for the calendar :')
    response=input("> ")
    

if response.isdecimal() and int(response) > 0:
    year = int(response)
    break

print('Please enter a numeric year, like 2023.')
continue



 
 