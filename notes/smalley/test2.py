import random

mylist = []
mylist.append(random.randint(0,2))
mylist.append(random.randint(0,2))
print(mylist)

for i in mylist:
    if i == 0:
        print("It is 0")
    elif i == 1:
        print("It might be 1")
    elif i == 2:
        print("Maybe 2")


