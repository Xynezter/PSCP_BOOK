"""Right Arrow"""
import math as m
def main():
    """Right Arrow"""
    k = int(input())
    n = int(input())
    mid = int(m.ceil(n / 2))
    for i in range(mid):
        print(" " * i + "*" * k)
    for i in range(mid - 1):
        print(" " * (mid -2 - i) + "*" * k)
main()
