"""Sequence VI"""
def main():
    """Sequence VI"""
    n = int(input())
    for i in range(1, n + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line)
main()
