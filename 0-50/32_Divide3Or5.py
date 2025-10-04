"""Divide3Or5"""
def main():
    """Divide3Or5"""
    num = int(input())
    total = 0
    for i in range(1, num + 1):
        if not i % 3:
            total += i
        elif not i % 5:
            total += i
    print(total)
main()
