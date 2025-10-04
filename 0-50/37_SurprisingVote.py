"""l"""
allnum = float(input())
maxnum = float(input())
midnum = allnum - maxnum
highestnum = min(maxnum, midnum)
minnie = midnum - highestnum
if maxnum - 2 > minnie:
    print("Surprising")
else:
    print("Not surprising")
