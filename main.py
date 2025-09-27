def is_leap_year(year: int) -> bool:
"""判断是否为闰年"""
if year % 400 == 0:
return True
if year % 100 == 0:
return False
if year % 4 == 0:
return True
return False

if **name** == "**main**":
try:
year_str = input().strip()
if not year_str:  # 空输入
print("输入错误")
else:
year = int(year_str)
if year < 0:
print("不是闰年")
elif is_leap_year(year):
print("是闰年")
else:
print("不是闰年")
except ValueError:
print("输入错误")

