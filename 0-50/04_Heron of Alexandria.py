"""Heron of Alexandria"""
a = float(input())
b = float(input())
c = float(input())
s = ( a + b + c ) / 2
Az = (s * (s-a) * (s-b) * (s-c)) ** (1/2)
print(f"{Az:.3f}")
