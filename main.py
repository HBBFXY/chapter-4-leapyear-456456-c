def is_leap_year(year: int) -> bool:
"""判断是否为闰年"""
return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if **name** == "**main**":
try:
year_str = input().strip()
year = int(year_str)  # 尝试转换为整数
if is_leap_year(year):
print("是闰年")
else:
print("不是闰年")
except Exception:
print("输入错误")


