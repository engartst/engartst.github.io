# Program to make a smooth transition of structuring processes from 
# Smalley 1997
# Stewart Engart, 20221229
# with random motion and growth processes
# with random behaviors
# with random spectral space

import json
import random
from datetime import date

random.seed(1)

# get the categories from the json file
with open('structProcess.json') as fp:
    data = json.load(fp)
with open('motionGrowth.json') as fp:
    motionList = json.load(fp)
with open('behavior.json') as fp:
    behaviorList = json.load(fp)
with open('specSpace.json') as fp:
    spaceList = json.load(fp)

# print all the stuff in the list
def print_interface(a):
    print(a+": ")
    print(data[a])
    print()
    print("---")
    print()


print("# SPECTROMORPHOLOGY")
print(f'## {date.today()}')
print()
all = ["Onset", "Continuation", "Termination"]
for i in all:
    print_interface(i)

# get user input for where to start/end
startOnsetIndex = int(input("Start onset index: "))
startOnset = data["Onset"][startOnsetIndex]
startContinuationIndex = int(input("Start continuation index: "))
startContinuation = data["Continuation"][startContinuationIndex]
startTerminationIndex = int(input("Start termination index: "))
startTermination = data["Termination"][startTerminationIndex]
print()
print("---")
print()
endOnsetIndex = int(input("End onset index: "))
endOnset = data["Onset"][endOnsetIndex]
endContinuationIndex = int(input("End continuation index: "))
endContinuation = data["Continuation"][endContinuationIndex]
endTerminationIndex = int(input("End termination index: "))
endTermination = data["Termination"][endTerminationIndex]
print()
print("---")
print()
COMMON = int(input("How many processes to keep in common between generations (1 or 2)?: "))
print()
print("---")
print()
defi = input("Do you want definitions (y or n)?: ")
print()
print("---")
print()

print(startOnset)
print(startContinuation)
print(startTermination)
print(random.choice(motionList["motion"]))
print(random.choice(behaviorList["causality"]))
print(random.choice(behaviorList["coordination"]))
print(random.choice(behaviorList["dominance"]))
print(random.choice(behaviorList["conflict"]))
print(random.choice(spaceList["specSpace"]))

# shuffle the lists with keeping the desired one in front
def shuffleList(a, b):
    a = a[b: ]+a[: b]
    copy = a[1: ]
    random.shuffle(copy)
    a[1: ] = copy
    return a

onsetList = shuffleList(data["Onset"], startOnsetIndex)
continuationList = shuffleList(data["Continuation"], startContinuationIndex)
terminationList = shuffleList(data["Termination"], startTerminationIndex)
endOnsetIndex = onsetList.index(endOnset)
endContinuationList = continuationList.index(endContinuation)
endTerminationList = terminationList.index(endTermination)

choiceList = range(3)
onsetLength = len(onsetList[: endOnsetIndex])
continuationLength = len(continuationList[: endContinuationIndex])
terminationLength = len(terminationList[: endTerminationIndex])
a = 0
b = 0
c = 0
z = 0

while z < len(all):
    magicList = []
    magic = random.choice(choiceList)
    magicList.append(magic)
    if COMMON == 1:
        magic = random.choice(choiceList)
        magicList.append(magic)
    else:
        pass

    motion = random.choice(motionList["motion"])
    print()
    print("---")
    print()
    # put it into a loop to so it can be flexible with how many strucProc stays
    # in common
    print(f'Change structProc {magicList}')
    for m in magicList:
        if m == 0 and a < onsetLength:
            a+=1
        elif m == 1 and b < continuationLength:
            b+=1
        elif m == 2 and c < terminationLength:
            c+=1
        elif a == onsetLength and b == continuationLength and c == terminationLength:
            print(endOnset)
            print(endContinuation)
            print(endTermination)
            print(motion)
            print(random.choice(behaviorList["causality"]))
            print(random.choice(behaviorList["coordination"]))
            print(random.choice(behaviorList["dominance"]))
            print(random.choice(behaviorList["conflict"]))
            print(random.choice(spaceList["specSpace"]))
            print()
            print("---")
            print()
            # added definitions to the end of the printing
            print()
            if defi == 'y':
                print("# DEFINITIONS")
                print()
                print("## ONSETS")
                print()
                print("departure: the action of leaving, especially to start a journey")
                print("emergence: the process of coming into view or becoming exposed after being concealed")
                print("anacrusis: 'delta' but also one or more unstressed notes before the first bar line of a piece or passage")
                print("attack: an aggressive and violent action against a person or place")
                print("upbeat: an unaccented beat preceding an accented beat")
                print("downbeat: an accented beat, usually the first of the bar")
                print()
                print("## CONTINUATIONS")
                print()
                print("passage: the act or process of moving through, under, over, or past something on the way from one place to another")
                print("transition: the process or a period of changing from one state or condition to another")
                print("prolongation: extension of the spatial length of something")
                print("maintanence:  process of maintaining or preserving someone or something")
                print("statement: the occurrence of a musical idea or motive within a composition")
                print()
                print("## TERMINATION")
                print()
                print("arrival: the emergence or appearance of a new development, phenomenon, or product")
                print("disappearance: the process or fact of something ceasing to exist or be in use")
                print("closure: a sense of resolution or conclusion at the end of an artistic work")
                print("release: allow or enable to escape from confinement; set free")
                print("resolution: the passing of a discord into a concord during the course of changing harmony")
                print("plane: a level of existence, thought, or development")
                print()
                print("## MOTION AND GROWTH")
                print()
                print("### UNI")
                print()
                print("ascent: a climb or walk to the summit of a mountain or hill")
                print("plane: a level of existence, thought, or development")
                print("descent: an action of moving downward, dropping, or falling")
                print()
                print("### RECIPROCAL")
                print()
                print("parabola: ")
                print("oscillation: movement back and forth at a regular speed")
                print("undulation: the action of moving smoothly up and down")
                print()
                print("### CYCLIC")
                print()
                print("rotation: the action of rotating around an axis or center")
                print("spiral: winding in a continuous and gradually widening (or tightening) curve")
                print("spin: rapid turning or whirling motion")
                print()
                print("### CENTRIC")
                print()
                print("vortex: a mass of whirling fluid or air, especially a whirlpool or whirlwind")
                print("pericentrality: arranged around a center")
                print("centrifugal motion: apparent outward force on a mass when it is rotated")
                print()
                print("### BI/MULTIDIRECTIONAL")
                print()
                print("agglomeration: a mass or collection of things")
                print("dissipation: to spread thin or scatter and gradually vanish")
                print("dilation: the act or action of enlarging, expanding, or widening")
                print("contraction: to draw together so as to become diminished in size")
                print("divergence: a drawing apart (as of lines extending from a common center)")
                print("convergence: independent development of similar traits or features (as of body structure or behavior) in unrelated or distantly related species or lineages")
                print("exogeny: the origins of existence of self, or the identity of self, emanating from, or sustaining, outside the natural or influenced realm")
                print("endogeny: processes that originate from within a living system such as an organism, tissue, or cell")
                print()
                print("## SPECTRAL SPACE")
                print()
                print("canopy: above 5,000Hz")
                print("center: 300Hz and 5,000Hz")
                print("root: below 300Hz")
            else:
                pass
            exit()
    else:
        pass
    print(onsetList[a])
    print(continuationList[b])
    print(terminationList[c])
    print(motion)
    print(random.choice(behaviorList["causality"]))
    print(random.choice(behaviorList["coordination"]))
    print(random.choice(behaviorList["dominance"]))
    print(random.choice(behaviorList["conflict"]))
    print(random.choice(spaceList["specSpace"]))
