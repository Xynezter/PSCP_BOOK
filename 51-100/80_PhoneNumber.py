"""PhoneNumber"""
phonenum = input()
c = input()
if c == "Domestic":
    if len(phonenum) == 10:
        print(phonenum[0:2], phonenum[2:6], phonenum[6:10])
    else:
        print(phonenum[0], phonenum[1:5], phonenum[5:9])
else:
    if len(phonenum) == 10:
        print(phonenum[0].replace("0", "+66") + phonenum[1], phonenum[2:6], phonenum[6:10])
    else:
        print(phonenum[0].replace("0", "+66"), phonenum[1:5], phonenum[5:9])
