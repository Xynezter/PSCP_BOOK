"""l"""
a = float(input())
b = int(input())
c = float(input())
if a < c:
    print(0)
else:
    ratio = a / c
    CUR = 1.0
    D = 0
    while CUR <= ratio:
        CUR *= b
        D += 1
    rockets = (b**D - 1) // (b - 1)
    print(rockets)
