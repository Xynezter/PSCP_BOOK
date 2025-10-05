"""Sequence VIII"""
n = int(input())
for i in range(1, n + 1):
    spaces = '   ' * (n - i)
    NUMBERS = ' '.join(f"{j:02d}" for j in range(1, i + 1))
    print(spaces + NUMBERS)
