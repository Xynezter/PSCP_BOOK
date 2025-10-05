"""l"""
allstr = tuple(input().split())
find = input()
index = allstr.index(find)
square = allstr.count(find)
for i in range(square):
    for j in range(square):
        if j == square - 1:
            print(index)
        else:
            print(index, end=" ")
    i += 0
