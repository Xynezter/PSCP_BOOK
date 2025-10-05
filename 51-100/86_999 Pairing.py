"""999 Pairing"""
def main():
    """999 Pairing"""
    range_ = int(input())
    num1 = input()
    num2 = input()
    wrong = sum(int(num1[i]) + int(num2[i]) != 9 for i in range(range_))
    if not wrong:
        print("YES")
    else:
        print(f"NO {wrong}")
main()
