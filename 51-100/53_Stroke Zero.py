"""Stroke Zero"""
def main():
    """Stroke Zero"""
    n = int(input())
    if n == 3:
        print("0")
        print("0 0")
        print("0 0 0")
    else:
        for i in range(1, n + 1):
            if i == 1:
                print("0")
            elif i == 2:
                print("0 0")
            elif i == n:
                print("0 " * (n-1) + "0")
            else:
                print("0 " + "1 " * (i - 2) + "0")
main()
