"""Century"""
n = int(input())
for _ in range(n):
    year = input().split()
    if len(year) != 2:
        print("ERROR")
        continue
    era, year1 = year
    if not year1.isdigit():
        print("ERROR")
        continue
    year1 = int(year1)
    if era == "B.E.":
        year1 -= 543
    elif era != "A.D.":
        print("ERROR")
        continue
    if year1 <= 0:
        print("ERROR")
        continue
    century = (year1 - 1) // 100 + 1
    _ = century
    print(_)
