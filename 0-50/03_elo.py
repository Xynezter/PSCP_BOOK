"""elo"""
RA = int(input())
RB = int(input())
tp = input()
EA = 1 / (1 + 10**((RB - RA)/400))
EB = 1 / (1 + 10**((RA - RB)/400))
if tp == "A":
    print(f"{EA:.2f}")
elif tp == "B":
    print(f"{EB:.2f}")
