"""l"""
def main():
    """l"""
    floor = int(input())
    sell = int(input())
    size = 1
    while True:
        totalorange = size * size
        if sell >= totalorange:
            sell -= totalorange
            floor -= 1
            size += 1
        else:
            break
    print(floor)
main()
