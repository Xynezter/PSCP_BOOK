"""f"""
alldict = {}
deaddict = {}
while True:
    string = input().strip("\"{,}").split("\" : \"")
    if string[0] != 'Start':
        alldict.update({string[0] : string[-1]})
    else:
        break
while True:
    dead = input()
    if dead != "End":
        deaddict[dead] = alldict.pop(dead)
    else:
        break
impostor_remains = list(alldict.values()).count("Impostor")
print(f"{impostor_remains} Impostor Remains")
print("***Alive***")
for name in sorted(alldict.keys()):
    print(f"{name} : {alldict[name]}")
print("***Dead***")
for name in sorted(deaddict.keys()):
    print(f"{name} : {deaddict[name]}")
