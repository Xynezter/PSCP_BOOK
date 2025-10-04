"""Ball"""
def main():
    """Ball"""
    n = float(input())
    n = n * 100
    count = 0
    if n < 1:
        print("0")
        return
    while n * 0.6 >= 1:
        n = n * 0.6
        count += 1
    print(count)
main()
