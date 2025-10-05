"""l"""
text = input()
LETTER = "abcdefghijklmnopqrstuvwxyz"
D = "".join(i + i.upper() for i in LETTER)
freq = {}
for i in text:
    if i.isalpha():
        freq[i] = freq.get(i, 0) + 1
for i in D:
    if i in freq:
        print(f"{i} = {freq[i]}")
