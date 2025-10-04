"""Sequence V"""
def main():
    """Sequence V"""
    n = int(input())
    count = 0
    for i in range(n, 0, -1):
        count += 1
        if not count % 7 or i == 1:
            print(i)
        else:
            print(i, end=" ")
main()
