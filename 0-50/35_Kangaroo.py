"""Kangaroo"""
def main():
    """Kangaroo"""
    k1 = int(input())
    k2 = int(input())
    k3 = int(input())
    result = 0
    if k1 > k2:
        k1, k2 = k2, k1
    if k1 > k3:
        k1, k3 = k3, k1
    if k2 > k3:
        k2, k3 = k3, k2
    if k2 - k1 >= k3 - k2:
        result = k2 - k1 - 1
    elif k3 - k2 >= k2 - k1:
        result = k3 - k2 - 1
    # if k1 < k2 < k3:
    # elif k1 > k2 > k3:
    #     if k2 - k3 > k1 - k2:
    #         result = k3 - k1 - 1
    #     elif k1 - k2 > k2 - k3:
    #         result = k1 - k2 - 1
    # elif k1 < k2 > k3:
    #     if k2 - k3 > k2 - k1:
    #         result = k2 - k3 - 1
    #     elif k2 - k1 > k2 - k3:
    #         result = k2 - k1 - 1
    print(result)
main()
