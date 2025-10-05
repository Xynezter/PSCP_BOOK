"""d"""
string1 = input()
string2 = input()
ham = sum(x != y for x, y in zip(string1, string2))
print(ham)
