"""BigFrame"""
def main():
    """BigFrame"""
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    s4 = input().strip()
    s5 = input().strip()
    maxs = max(len(s1), len(s2), len(s3), len(s4), len(s5))
    print("*" * (maxs + 4))
    print("* " + s1.ljust(maxs) + " *")
    print("* " + s2.ljust(maxs) + " *")
    print("* " + s3.ljust(maxs) + " *")
    print("* " + s4.ljust(maxs) + " *")
    print("* " + s5.ljust(maxs) + " *")
    print("*" * (maxs + 4))
main()
