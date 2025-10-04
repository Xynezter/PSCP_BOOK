"""Heads and Legs"""
def main():
    """Heads and Legs"""
    a = int(input())
    b = int(input())
    r = (b - 2 * a) // 2
    bird = a - r
    if (b - 2 * a) % 2:
        print("Impossible")
        return
    if r < 0 or bird < 0:
        print("Impossible")
    else:
        print(r, bird)
main()
