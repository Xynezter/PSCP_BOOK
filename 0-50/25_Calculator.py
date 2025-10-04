"""Calculator"""
def main():
    """Calculator"""
    n = int(input())
    count = 0
    if n == 1:
        print(1)
    else:
        for i in range(1, n + 1):
            g = len(str(i))
            count += g + 1
        print(count)
main()
