"""Sequence IV"""
def main():
    """Sequence IV"""
    n = int(input())
    for i in range(n):
        i = i * n
        for j in range(1, n + 1):
            if j == n:
                print(i + j)
            else:
                print(i + j, end=" ")
main()
