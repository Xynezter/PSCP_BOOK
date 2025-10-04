"""Temperature"""
def to(tem,f, s):
    """Temperature"""
    f = f.upper()
    s = s.upper()
    result = 0
    if f.upper() == "C" and s.upper() == "F":
        result += ((tem * 9) / 5) + 32
        print(f"{result:.2f}")
    elif f.upper() == "C" and s.upper() == "K":
        result += tem + 273.15
        print(f"{result:.2f}")
    elif f.upper() == "C" and s.upper() == "R":
        result += (tem + 273.15) * (9 / 5)
        print(f"{result:.2f}")
    elif f.upper() == "F" and s.upper() == "C":
        result += (5 / 9 * (tem - 32))
        print(f"{result:.2f}")
    elif f.upper() == "F" and s.upper() == "K":
        result += ((tem - 32) * (5 / 9)) +273.15
        print(f"{result:.2f}")
    elif f.upper() == "F" and s.upper() == "R":
        result += tem + 459.67
        print(f"{result:.2f}")
    elif f.upper() == "K" and s.upper() == "C":
        result += tem - 273.15
        print(f"{result:.2f}")
    elif f.upper() == "K" and s.upper() == "F":
        result += ((9 / 5) * (tem - 273.15)) + 32
        print(f"{result:.2f}")
    elif f.upper() == "K" and s.upper() == "R":
        result += tem * (9 / 5)
        print(f"{result:.2f}")
    elif f.upper() == "R" and s.upper() == "C":
        result += (tem - 491.67) * (5 / 9)
        print(f"{result:.2f}")
    elif f.upper() == "R" and s.upper() == "F":
        result += tem - 459.67
        print(f"{result:.2f}")
    elif f.upper() == "R" and s.upper() == "K":
        result += tem * (5 / 9)
        print(f"{result:.2f}")
def main():
    """Temperature"""
    tem = float(input())
    f = input()
    s = input()
    if f.upper() == s.upper():
        print(f"{tem:.2f}")
        return
    to(tem, f, s)
main()
