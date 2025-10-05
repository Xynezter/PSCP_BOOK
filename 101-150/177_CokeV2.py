"""Coke"""
def main():
    """Coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        totalprice = a * d
        print(totalprice)
    elif not d:
        print(0)
    else:
        disbottal = (d - 1) // b
        totalprice = (d - disbottal) * a + disbottal * c
        print(totalprice)
main()
