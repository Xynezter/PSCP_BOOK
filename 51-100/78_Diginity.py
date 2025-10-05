"""l"""
while True:
    N = input()
    RESULT = 0
    if N != "0":
        while len(N) >= 2:
            for i in N:
                RESULT += int(i)
            N = str(RESULT)
            RESULT = 0
        print(N)
    else:
        break
