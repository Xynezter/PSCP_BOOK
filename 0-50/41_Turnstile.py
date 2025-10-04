"""Turnstile"""
def main():
    """l"""
    status = 0
    count = 0
    while True:
        action = input()
        if action == "C" and not status:
            status += 1
        elif action == "P" and status == 1:
            status -= 1
            count += 1
        elif action == "END":
            break
    print(count)
main()
