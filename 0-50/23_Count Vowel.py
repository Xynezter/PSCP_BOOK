"""Count Vowel"""
def main():
    """Count Vowel"""
    r = int(input())
    count = 0
    for _ in range(r):
        a = input()
        if a.upper() == "A" or a.upper() == "E" or\
            a.upper() == "I" or a.upper() == "O" or a.upper() == "U":
            count +=1
    print(count)
main()
