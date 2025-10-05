"""Grocery"""
def main():
    """Grocery"""
    veg = input()
    realveg = veg.split()
    total = int(realveg[0]) * 10 + int(realveg[1]) * 25 + int(realveg[2]) * 3
    print(total)
main()
