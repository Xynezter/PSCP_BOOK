"""Squid Game 3 - Tug-of-War"""
def main():
    """Squid Game 3 - Tug-of-War0"""
    totala = 0
    totalb = 0
    count = 0
    while count < 20:
        num = int(input())
        if count < 10:
            totala += num
        else:
            totalb += num
        count +=1
    if totala == totalb:
        print("AB")
    elif totala > totalb:
        print("B")
    else:
        print("A")
main()
