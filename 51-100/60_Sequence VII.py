"""Sequence VII"""
def main():
    """Sequence VII"""
    n = int(input())
    for i in range(1, n + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line)
    for i in range(n - 1, 0, -1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line)
main()
