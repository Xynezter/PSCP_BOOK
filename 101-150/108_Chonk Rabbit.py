"""Chonk Rabbit"""
def main():
    """Chonk Rabbit"""
    n = int(input())
    maxcha = [0, 0]
    counter = 0
    for _ in range(n):
        cha = input().split()
        if int(cha[1]) > 15:
            counter += 1
        if int(maxcha[1]) < int(cha[1]):
            maxcha = cha
    print(counter)
    for i in maxcha:
        print(i + " ",end="")
main()
