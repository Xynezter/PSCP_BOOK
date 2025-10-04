"""FOR!F-Ball"""
def main():
    """l"""
    move = input().upper()
    count = 1
    for i in move:
        if i == "A":
            if count == 1:
                count = 2
            elif count == 2:
                count = 1
        if i == "B":
            if count == 2:
                count = 3
            elif count == 3:
                count = 2
        if i == "C":
            if count == 1:
                count = 3
            elif count == 3:
                count = 1
    print(count)
main()
