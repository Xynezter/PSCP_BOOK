"""Backward"""
def main():
    """Backward"""
    allc = []
    while True:
        c = input()
        if c != "NULL":
            allc += [c]
        else:
            break
    for i in range(len(allc)):
        print(allc[-1 - i])
main()
