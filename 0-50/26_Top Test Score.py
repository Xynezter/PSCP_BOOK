"""Top Test Score"""
def main():
    """Top Test Score"""
    stu = int(input())
    count = 1
    hnum = -1
    for _ in range(stu):
        num = int(input())
        if num > hnum:
            hnum -= hnum
            hnum += num
        elif num == hnum:
            count += 1
    print(hnum)
    print(count)
main()
