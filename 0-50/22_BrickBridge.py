"""f"""
a = int(input())
b = int(input())
goal = int(input())
use_big = min(b, goal // 5)
remaining = goal - use_big * 5
if remaining <= a:
    print(remaining)
else:
    print(-1)
