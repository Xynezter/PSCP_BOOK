"""ฉันจะเป็น Saitama ให้ได้เลย"""
def main():
    """ฉันจะเป็น Saitama ให้ได้เลย"""
    pushup = int(input())
    situp = int(input())
    sit = int(input())
    run = int(input())
    pushup1 = int(input())
    situp1 = int(input())
    run1 = int(input())
    sit1 = int(input())
    daypush = (pushup + pushup1 - 1) // pushup1
    daysitup = (situp + situp1 - 1) // situp1
    daysit = (sit + sit1 - 1) // sit1
    dayrun = (run + run1 - 1) // run1
    totalday = daypush
    if daysitup > totalday:
        totalday = daysitup
    if daysit > totalday:
        totalday = daysit
    if dayrun > totalday:
        totalday = dayrun
    print(totalday)
main()
