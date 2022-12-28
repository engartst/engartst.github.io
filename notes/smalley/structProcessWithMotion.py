# Program to make a smooth transition of structuring processes from 
# Smalley 1997
# Stewart Engart, 20221228
# with random motion and growth processes

import json
import random

random.seed(1)

# get the categories from the json file
with open('structProcess.json') as fp:
    data = json.load(fp)

with open('motionGrowth.json') as fp:
    motionList = json.load(fp)

# print all the stuff in the list
def print_interface(a):
    print(a+":")
    print(data[a])
    print("-----")

all = ["Onset", "Continuation", "Termination"]
for i in all:
    print_interface(i)

# get user input for where to start/end
startOnsetIndex = int(input("Start onset index:"))
startOnset = data["Onset"][startOnsetIndex]
startContinuationIndex = int(input("Start continuation index:"))
startContinuation = data["Continuation"][startContinuationIndex]
startTerminationIndex = int(input("Start termination index:"))
startTermination = data["Termination"][startTerminationIndex]
print("-----")
endOnsetIndex = int(input("End onset index:"))
endOnset = data["Onset"][endOnsetIndex]
endContinuationIndex = int(input("End continuation index:"))
endContinuation = data["Continuation"][endContinuationIndex]
endTerminationIndex = int(input("End termination index:"))
endTermination = data["Termination"][endTerminationIndex]
print("/////")

print(startOnset)
print(startContinuation)
print(startTermination)
print(random.choice(motionList["motion"]))

# shuffle the lists with keeping the desired one in front
def shuffleList(a, b):
    a = a[b:]+a[:b]
    copy = a[1:]
    random.shuffle(copy)
    a[1:] = copy
    return a

onsetList = shuffleList(data["Onset"], startOnsetIndex)
continuationList = shuffleList(data["Continuation"], startContinuationIndex)
terminationList = shuffleList(data["Termination"], startTerminationIndex)
endOnsetIndex = onsetList.index(endOnset)
endContinuationList = continuationList.index(endContinuation)
endTerminationList = terminationList.index(endTermination)


dumbList = range(3)
onsetLength = len(onsetList[:endOnsetIndex])
continuationLength = len(continuationList[:endContinuationIndex])
terminationLength = len(terminationList[:endTerminationIndex])
a = 0
b = 0
c = 0
z = 0

while z < len(all):
    magic = random.choice(dumbList)
    motion = random.choice(motionList["motion"])
    #print(f'Magic = {magic}')
    print('-----')
    if magic == 0 and a < onsetLength:
        a+=1
    elif magic == 1 and b < continuationLength:
        b+=1
    elif magic == 2 and c < terminationLength:
        c+=1
    elif a == onsetLength and b == continuationLength and c == terminationLength:
        print(endOnset)
        print(endContinuation)
        print(endTermination)
        print(motion)
        print('/////')
        exit()
    else:
        pass
    print(onsetList[a])
    print(continuationList[b])
    print(terminationList[c])
    print(motion)

