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
# 空输入
if not year_str:
print("输入错误")
else:
year = int(year_str)
if year < 0:  # 负年份直接不是闰年
print("不是闰年")
else:
print("是闰年" if is_leap_year(year) else "不是闰年")
except ValueError:
# 输入不是整数（例如字母、小数）
print("输入错误")

