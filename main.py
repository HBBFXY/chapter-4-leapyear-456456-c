
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def main():
    try:
        s = input().strip()
        if not s:
            print("输入错误")
            return
        year = int(s)
        if year < 0:
            print("不是闰年")
        elif is_leap_year(year):
            print("是闰年")
        else:
            print("不是闰年")
    except ValueError:
        print("输入错误")

if __name__ == "__main__":
    main()
