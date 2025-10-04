"""Sequence II"""
def main():
    """Sequence II"""
    step = int(input())
    for i in range(step):
        for x in range(0, step):
            if x == step - 1:
                print(i + x * step)
            else:
                print(i + x * step, end=" ")
main()
