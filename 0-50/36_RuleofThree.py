"""RuleofThree"""
def main():
    """RuleofThree"""
    totalsnack = int(input())
    maxprice = 0
    num = []
    for _ in range(1, totalsnack + 1):
        price = float(input())
        weight = float(input())
        if weight / price > maxprice:
            maxprice = weight / price
            num = [f"{price:.2f}", f"{weight:.2f}"]
        elif weight / price == maxprice:
            if price < float(num[0]):
                num = [f"{price:.2f}", f"{weight:.2f}"]
    for i in num:
        print(i, end=" ")
main()
