"""l"""
n = int(input())
allgiraff = []
COUNT = 0
for i in range(n):
    allgiraff.append(int(input()))
if n == 1:
    COUNT = 1
else:
    for i in range(n):
        if not i:
            if allgiraff[i] > allgiraff[i + 1]:
                COUNT += 1
        elif i == n - 1:
            if allgiraff[i] > allgiraff[i - 1]:
                COUNT += 1
        else:
            if allgiraff[i] > allgiraff[i - 1] and allgiraff[i] > allgiraff[i + 1]:
                COUNT += 1
print(COUNT)
