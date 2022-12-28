import random

mylist = range(3)
i = [0, 1, 2, 3, 4]
j = [5, 6, 7, 8, 9]
k = [10, 11, 12, 13, 14]
a = 0
b = 0
c = 0

while a < len(k):
    magic = random.choice(mylist)
    print(f'Magic = {magic}')
    if magic == 0 and a < 3:
        a+=1
    elif magic == 1 and b < 3:
        b+=1
    elif magic == 2 and c < 3:
        c+=1
    if a==3 and b==3 and c==3:
        exit()
    else:
        pass
    print(i[a])
    print(j[b])
    print(k[c])

