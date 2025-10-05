"""l"""
import math as m
n = int(input())
SCORE = 0
for i in range(n):
    pos = input().split(" ")
    x, y = pos[0], pos[1]
    distance = m.sqrt(int(x) ** 2 + int(y) ** 2)
    if distance <= 2.0:
        SCORE += 5
    elif distance <= 4.0:
        SCORE += 4
    elif distance <= 6.0:
        SCORE += 3
    elif distance <= 8.0:
        SCORE += 2
    elif distance <= 10.0:
        SCORE += 1
    i += 0
print(SCORE)
