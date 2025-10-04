"""Pongya"""
def main():
    """PongYa"""
    p =int(input())
    count = 0
    if not p % 3 or p % 10 == 3:
        print("PONG")
    else:
        for i in range(1, p+1):
            if not i % 3:
                count += 1
            else:
                count += 1
        print(count)
main()
