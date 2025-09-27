def is_leap_year(year: int) -> bool:
"""Check if a year is a leap year"""
return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if **name** == "**main**":
try:
year_str = input().strip()
year = int(year_str)
if is_leap_year(year):
print("Leap year")
else:
print("Not a leap year")
except Exception:
print("Invalid input")

