"""Left Arrow"""
import math as m
def main():
    """Left Arrow"""
    k = int(input())
    n = int(input())
    mid = m.ceil(n / 2)
    for i in range(1, n + 1):
        if i < mid:
            spaces = mid - i
        else:
            spaces = i - mid
        print(" " * spaces + "*" * k)
main()
