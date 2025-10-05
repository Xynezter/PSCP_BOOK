"""PickThemAgain"""
ALLNUM = input().split()
ALLNUM.reverse()
num = []
for i in ALLNUM:
    if not int(i) % 3 or not int(i) % 5:
        num.append(i)
if num:
    for i in num:
        print(i)
else:
    print("Nope")
