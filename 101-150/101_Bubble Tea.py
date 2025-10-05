"""Bubble Tea"""
def rose(lv, v, vb, bubble):
    """Bubble Tea"""
    if lv == "1":
        if bubble == "H":
            print(f"{(12 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(12 * v) + (3 * vb)}")
        else:
            print(f"{(12 * v) + (2 * vb)}")
    elif lv == "2":
        if bubble == "H":
            print(f"{(18 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(18 * v) + (3 * vb)}")
        else:
            print(f"{(18 * v) + (2 * vb)}")
    elif lv == "3":
        if bubble == "H":
            print(f"{(25 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(25 * v) + (3 * vb)}")
        else:
            print(f"{(25 * v) + (2 * vb)}")

def taiwan(lv, v, vb, bubble):
    """Bubble Tea"""
    if lv == "1":
        if bubble == "H":
            print(f"{(15 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(15 * v) + (3 * vb)}")
        else:
            print(f"{(15 * v) + (2 * vb)}")
    elif lv == "2":
        if bubble == "H":
            print(f"{(20 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(20 * v) + (3 * vb)}")
        else:
            print(f"{(20 * v) + (2 * vb)}")
    elif lv == "3":
        if bubble == "H":
            print(f"{(30 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(30 * v) + (3 * vb)}")
        else:
            print(f"{(30 * v) + (2 * vb)}")

def macha(lv, v, vb, bubble):
    """Bubble Tea"""
    if lv == "1":
        if bubble == "H":
            print(f"{(10 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(10 * v) + (3 * vb)}")
        else:
            print(f"{(10 * v) + (2 * vb)}")
    elif lv == "2":
        if bubble == "H":
            print(f"{(15 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(15 * v) + (3 * vb)}")
        else:
            print(f"{(15 * v) + (2 * vb)}")
    elif lv == "3":
        if bubble == "H":
            print(f"{(20 * v) + (5 * vb)}")
        elif bubble == "O":
            print(f"{(20 * v) + (3 * vb)}")
        else:
            print(f"{(20 * v) + (2 * vb)}")

def main():
    """Bubble Tea"""
    bubble, vb = input().split()
    tea, lv, v = input().split()
    vb = int(vb)
    v = int(v)
    if tea.upper() == "R":
        rose(lv, v, vb, bubble)
    elif tea.upper() == "T":
        taiwan(lv, v, vb, bubble)
    elif tea.upper() == "M":
        macha(lv, v, vb, bubble)
main()
