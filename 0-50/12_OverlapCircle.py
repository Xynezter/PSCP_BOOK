"""OverlapCircle"""
def main():
    """OverlapCircle"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    d = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    sumr = r1 + r2
    if d <= sumr:
        print("overlapping")
    else:
        print("no overlapping")
main()
