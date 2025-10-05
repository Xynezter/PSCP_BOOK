"""l"""
s = int(input())
text = input()
DECODED = ""
for c in text:
    if 'A' <= c <= 'Z':
        DECODED += chr((ord(c) - ord('A') + s) % 26 + ord('A'))
    elif 'a' <= c <= 'z':
        DECODED += chr((ord(c) - ord('a') + s) % 26 + ord('a'))
    else:
        DECODED += c
print(DECODED)
