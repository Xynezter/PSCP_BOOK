"""ProgressiveTax"""
def a(num, total):
    """l"""
    total += ((num - 4000000) * 0.35) + (2000000 * 0.3) + (1000000 * 0.25) + \
(250000 * 0.2) + (250000 * 0.15) + (200000 * 0.1) + (150000 * 0.05)
    print(int(total))

def b(num, total):
    """l"""
    total += ((num - 2000000) * 0.3) + (1000000 * 0.25) + (250000 * 0.2) + \
(250000 * 0.15) + (200000 * 0.1) + (150000 * 0.05)
    print(int(total))

def c(num, total):
    """l"""
    total += ((num - 1000000) * 0.25) + (250000 * 0.2) + (250000 * 0.15) + \
(200000 * 0.1) + (150000 * 0.05)
    print(int(total))

def d(num, total):
    """l"""
    total += ((num - 750000) * 0.2) + (250000 * 0.15) + (200000 * 0.1) + (150000 * 0.05)
    print(int(total))

def e(num, total):
    """l"""
    total += ((num - 500000) * 0.15) + (200000 * 0.1) + (150000 * 0.05)
    print(int(total))

def f(num, total):
    """l"""
    total += ((num - 300000) * 0.10) + (150000 * 0.05)
    print(int(total))

def g(num, total):
    """l"""
    total += ((num - 150000) * 0.05)
    print(int(total))

def main():
    """ProgressiveTax"""
    num = int(input())
    total = 0
    if num > 4000000:
        a(num, total)
    elif 2000000 < num <= 4000000:
        b(num, total)
    elif 1000000 < num <= 2000000:
        c(num, total)
    elif 750000 < num <= 1000000:
        d(num, total)
    elif 500000 < num <= 750000:
        e(num, total)
    elif 300000 < num <= 500000:
        f(num, total)
    elif 150000 < num <= 300000:
        g(num, total)
    else:
        print("0")
main()
