"""l"""
n = int(input())
bowl = [int(input()) for _ in range(n)]
freq = {}
for x in bowl:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(max(freq.values()))
