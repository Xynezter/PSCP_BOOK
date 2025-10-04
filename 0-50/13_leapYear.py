"""leapYear"""
def main():
    """leapYear"""
    y = int(input())
    if not y % 100:
        if not y % 400:
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")
    elif not y % 4:
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")
main()
