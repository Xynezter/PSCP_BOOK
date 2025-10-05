"""f"""
def main():
    """f"""
    n = int(input())
    lnum = []
    num = input().split()
    counter = 0
    maxnum = 0
    result = 0
    for i in num:
        lnum.append(i)
    for i in lnum:
        if int(i) == int(lnum[-1]) and n == 1:
            maxnum = int(lnum[0])
            if maxnum > int(lnum[-1]):
                print(maxnum)
            else:
                print(lnum[-1])
        else:
            counter += 1
            if int(maxnum) < int(i):
                maxnum = i
            if counter >= 2:
                result += int(maxnum)
                if int(i) == int(lnum[-1]):
                    print(maxnum,"=" , result, end="")
                else:
                    print(maxnum, "+ ", end="")
                maxnum = 0
                counter = 0
main()
