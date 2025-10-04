"""d"""
def main():
    """j"""
    m = int(input())
    n = int(input())
    count = 0
    for _ in range(1, m+1):
        for i in range(1, n+1):
            count += 1
            if i == n:
                print(count)
            else:
                print(count,end=" ")
main()
