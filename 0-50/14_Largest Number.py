"""l"""
a = input()
b = input()
c = input()

def bigger(x, y):
    """l"""
    return x + y >= y + x

if bigger(a, b):
    first, second = a, b
else:
    first, second = b, a

if bigger(c, first):
    result = c + first + second
elif bigger(c, second):
    result = first + c + second
else:
    result = first + second + c

if not result.strip('0'):
    print('0')
else:
    print(result)
