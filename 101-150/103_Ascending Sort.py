"""Ascending Sort"""
def main():
    """Ascending Sort"""
    n = int(input())
    nums = []
    for _ in range(n):
        num = int(input())
        nums += [num]
    nums.sort()
    for i in nums:
        print(i)
main()
