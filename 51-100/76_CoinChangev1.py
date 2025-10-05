"""CoinChangev1"""
def main():
    """CoinChangev1"""
    price1 = int(input())
    coin = 0
    while price1 > 0:
        if price1 >= 25:
            coin += price1 // 25
            price1 -= 25 * (price1 // 25)
        elif price1 >= 10:
            coin += price1 // 10
            price1 -= 10 * (price1 // 10)
        elif price1 >= 5:
            coin += price1 // 5
            price1 -= 5 * (price1 // 5)
        else:
            coin += 1
            price1 -= 1
    print(coin)
main()
