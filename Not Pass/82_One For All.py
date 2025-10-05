"""l"""
n = int(input())
S = ""
for i in range(n):
    name = input()
    if not i:
        S += name
    else:
        sep = "*" * i if i % 2 else "-" * i
        S += sep + name
S += f"_{n}"
print(S)
