"""3nPlus1"""
def main():
    """3nPlus1"""
    count = 1
    while True:
        n = int(input())
        if n > 0:
            while True:
                if n == 1.0:
                    print(count)
                    count = 1
                    break
                if not n % 2:
                    count += 1
                    n = n/2
                elif n % 2 and n > 1:
                    count += 1
                    n = n * 3 + 1
        else:
            break
main()
