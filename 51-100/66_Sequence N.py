"""Sequence N"""
m = int(input())
for i in range(m):
    LINE = ""
    for j in range(m):
        if j in (0, m - 1, i):
            LINE += "*"
        else:
            LINE += " "
    print(LINE)
