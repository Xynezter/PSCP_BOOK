"""Matrix_MN"""
M = int(input())
N = int(input())
ALLNUM = []
COUNTER = 0
for i in range(M * N):
    num = input()
    ALLNUM.append(num)
for i in ALLNUM:
    COUNTER += 1
    if COUNTER <= N:
        if COUNTER == N:
            print(i)
            COUNTER = 0
        else:
            print(i, end=" ")
