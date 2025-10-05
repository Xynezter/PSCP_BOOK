'''Key'''
def main():
    '''code'''
    x = input()
    sumx = sum(int(i) for i in x)
    last = int(x[10:14]) * 10
    total = sumx + last
    if total < 1000:
        print(total + 1000)
    elif total >= 10000:
        print(str(total)[1:])
    else:
        print(total)
main()
