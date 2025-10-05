"""fiveX"""
def main():
    """fiveX"""
    num = int(input())
    x = 0
    for _ in range(num):
        if x < 4:
            print("*", end= "")
            x += 1
        else:
            print("X", end= "")
            x = 0
main()
