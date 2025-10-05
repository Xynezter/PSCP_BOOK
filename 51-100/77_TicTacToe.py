"""Dw"""
xo1 = input()
xo2 = input()
xo3 = input()
if xo1[0] == xo1[1] == xo1[2] and xo1[0] != "-":
    print(xo1[0], "WIN")
elif xo2[0] == xo2[1] == xo2[2]and xo2[0] != "-":
    print(xo2[0], "WIN")
elif xo3[0] == xo3[1] == xo3[2]and xo3[0] != "-":
    print(xo3[0], "WIN")
elif xo1[0] == xo2[0] == xo3[0]and xo1[0] != "-":
    print(xo1[0], "WIN")
elif xo1[1] == xo2[1] == xo3[1]and xo1[1] != "-":
    print(xo1[1], "WIN")
elif xo1[2] == xo2[2] == xo3[2]and xo1[2] != "-":
    print(xo1[2], "WIN")
elif xo1[0] == xo2[1] == xo3[2]and xo1[0] != "-":
    print(xo1[0], "WIN")
elif xo1[2] == xo2[1] == xo3[0]and xo1[2] != "-":
    print(xo1[0], "WIN")
else:
    print("DRAW")
