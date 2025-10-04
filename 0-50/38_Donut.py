"""(Recommend) Donut"""
def main():
    """(Recommend) Donut"""
    costdonut = int(input())
    promotion = int(input())
    free = int(input())
    wantdonut = int(input())
    countdonut = 0
    promotioncount = 0
    totalprice = 0
    while countdonut < wantdonut:
        promotioncount += 1
        countdonut += 1
        totalprice += costdonut
        if promotioncount == promotion:
            countdonut += free
            promotioncount = 0
        # if countdonut >= wantdonut:
        #     break
        # if promotioncount >= 0:
        #     promotioncount += 1
        #     countdonut += 1
        #     if not promotioncount % promotion:
        #         promotioncount = 0
        #         countdonut += free
        #         totalprice += costdonut
        #     else:
        #         totalprice += costdonut
    print(totalprice, countdonut)
main()
