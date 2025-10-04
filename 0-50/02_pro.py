"""Pro"""

X = int(input())
Y = int(input())
A = int(input())
Z = int(input())

W = X - Y
J = Z // X * W
J1 = (Z * A) - (J * A)

print(int(J1))
