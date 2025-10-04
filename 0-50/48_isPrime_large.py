"""l"""
n = int(input())
PRIME = True
D = 2
if n < 2:
    print("NO")
else:
    while D <= n**0.5:
        if not n % D:
            PRIME = False
            break
        D += 1
    if PRIME:
        print("YES")
    else:
        print("NO")
