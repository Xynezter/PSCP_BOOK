"""BTSMRT"""
def children(age, h):
    """BTSMRT"""
    if age < 14 and h < 90:
        print("FREE")
    elif age < 14 and h <= 140:
        print("FREE")
    else:
        print("PAY")

def senior(age, h):
    """BTSMRT"""
    if age < 14 and h < 90:
        print("FREE")
    elif age >= 60:
        print("FREE")
    else:
        print("PAY")

def normal(age, h):
    """BTSMRT"""
    if age < 14 and h < 90:
        print("FREE")
    else:
        print("PAY")

def main():
    """BTSMRT"""
    day = input()
    age = float(input())
    h = float(input())
    if day == "Children Day":
        children(age, h)
    elif day == "Senior Day":
        senior(age, h)
    else:
        normal(age, h)
main()
