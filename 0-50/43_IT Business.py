"""l"""
bank = float(input())
havemoney = float(input())
FAIL = 0

while True:
    active = input()
    if active == "end":
        break
    action = active[0]
    value = float(active[2:])
    if action == "D":
        if havemoney >= value:
            havemoney -= value
            bank += value
            FAIL = 0
        else:
            FAIL += 1
    elif action == "W":
        if bank >= value:
            bank -= value
            havemoney += value
            FAIL = 0
        else:
            FAIL += 1
    if FAIL == 3:
        break

print(f"{bank:.2f}")
print(f"{havemoney:.2f}")
