"""Safe Password"""
def main():
    """Safe Password"""
    C = input()
    N = input()
    if C == "H" and N == "4567":
        print("safe unlocked")
    elif C == "H":
        print("safe locked - change digit")
    elif N == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")
main()
