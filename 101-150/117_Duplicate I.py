"""l"""
m = int(input())
n = int(input())
group1 = []
group2 = []
d = []
for i in range(1, m + n + 1):
    num = int(input())
    if i <= m:
        group1.append(num)
    else:
        group2.append(num)
for x in group1:
    if x in group2:
        d.append(x)
d.sort(key=int, reverse=True)
if not d:
    print("Nope")
else:
    for i in d:
        print(i)
