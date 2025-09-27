def is_leap_year(year: int) -> bool:
"""判断是否为闰年"""
return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if **name** == "**main**":
try:
year_str = input().strip()
if not year_str:
print("输入错误")
else:
year =
