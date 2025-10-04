"""Christmas Light"""
def main():
    """Christmas Light"""
    light = input().upper()
    n = int(input())
    count = 1
    rules = {'R': ['Red', 'Green', 'Blue'],
             'G': ['Green', 'Blue', 'Red'],
             'B': ['Blue', 'Red', 'Green']}
    colors = rules[light]
    for _ in range(n):
        if not count % 3:
            print(colors[2], end=" ")
            count -= 2
        elif not count % 2:
            print(colors[1], end=" ")
            count += 1
        else:
            print(colors[0], end=" ")
            count += 1
main()
