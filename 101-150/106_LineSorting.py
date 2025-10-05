"""LineSorting"""
N = int(input())
TEXT = []
for i in range(N):
    i = input()
    TEXT.append(i)
    TEXT.sort(key=len)
for i in TEXT:
    print(i)
