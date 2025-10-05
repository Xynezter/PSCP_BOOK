"""l"""
n = int(input())
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    row = []
    for j in range(1, i + 1):
        row.append(f"{j:02d}")
    for j in range(i - 1, 0, -1):
        row.append(f"{j:02d}")
    print(" ".join(row))
for i in range(n - 1, 0, -1):
    print("   " * (n - i), end="")
    row = []
    for j in range(1, i + 1):
        row.append(f"{j:02d}")
    for j in range(i - 1, 0, -1):
        row.append(f"{j:02d}")
    print(" ".join(row))
