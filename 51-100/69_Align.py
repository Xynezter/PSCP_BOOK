"""a"""
a = int(input())
n = input()
text = input()
match n:
    case "left":
        print(text.ljust(a, ' '))
    case "center":
        if len(text) % 2 and not a % 2:
            left_padding = (a - len(text)) // 2 + 1
            right_padding = a - len(text) - left_padding
            print(' ' * left_padding + text + ' ' * right_padding)
        else:
            print(text.center(a, ' '))
    case "right":
        print(text.rjust(a, ' '))
