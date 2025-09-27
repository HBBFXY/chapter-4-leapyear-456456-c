```python
def is_leap_year(year: int) -> bool:
    """判断是否为闰年"""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def main():
    try:
        user_input = input().strip()
        # 输入为空
        if not user_input:
            print("输入错误")
            return
        
        # 尝试转为整数
        year = int(user_input)
        
        # 负年份直接按“不是闰年”处理
        if year < 0:
            print("不是闰年")
            return
        
        # 判断闰年
        if is_leap_year(year):
            print("是闰年")
        else:
            print("不是闰年")
    except ValueError:
        # 输入不能转为整数时
        print("输入错误")

if __name__ == "__main__":
    main()
```
