"""GCD_N"""
import math as m
def main():
    """GCD_N"""
    count = int(input())
    allnum = []
    result = 0
    for _ in range(1, count + 1):
        num = int(input())
        allnum += [num]
    fristnum = int(allnum[0])
    for i in allnum:
        if 1 < i < 3:
            result = m.gcd(fristnum, i)
        elif i >= 3:
            result = m.gcd(result, i)
    print(result)
main()
