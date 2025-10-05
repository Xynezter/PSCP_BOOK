"""l"""
n = int(input())
allnum = []
missing = []
while True:
    num = int(input())
    allnum.append(num)
    if not num:
        break
allnum.sort()
for i in range(1, n + 1):
    if i not in allnum:
        missing.append(i)
for i in missing:
    print(i)
