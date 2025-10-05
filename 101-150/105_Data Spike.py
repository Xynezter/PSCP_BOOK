"""Data Spike"""
MAX_VALUE = -10**9
for _ in range(8):
    n = int(input())
    if n > MAX_VALUE:
        MAX_VALUE = n
    _ = MAX_VALUE
print(_)
