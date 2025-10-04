"""Bill"""
def main():
    """Bill"""
    price = int(input())
    dis = price * 0.1
    disserve = 0
    if dis < 50 :
        disserve += 50
        serve = price + disserve
        disvat = serve * 0.07
        total = serve + disvat
        print(f"{total:.2f}")
    elif dis >= 1000 :
        disserve += 1000
        serve = price + disserve
        disvat = serve * 0.07
        total = serve + disvat
        print(f"{total:.2f}")
    else :
        disserve += dis
        serve = price + disserve
        disvat = serve * 0.07
        total = serve + disvat
        print(f"{total:.2f}")
main()
