"""l"""
import json
def is_even(x):
    """f"""
    return not x % 2
numbers = json.loads(input())
xs = list(filter(is_even, numbers))
if len(xs) > 0:
    for n in xs:
        print(n)
else:
    print("Nope")
