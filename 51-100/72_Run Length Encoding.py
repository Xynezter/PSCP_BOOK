"""(Recommend) Run Length Encoding"""
def main():
    """(Recommend) Run Length Encoding"""
    charrector = input()
    run = charrector[0]
    count = 0
    last = {}
    for i in charrector:
        if run != i:
            print(str(count) + run, end="")
            count = 1
        elif run == i:
            count += 1
        run = i
        last = i
    print(str(count) + last)
main()
