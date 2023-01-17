# Program to do parsimonious voice leading
# Stewart Engart, 20230113

import json
import random
from datetime import date

random.seed(1)

# Constants
_key = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
_accidental = ['#', 'b', 'n']
_quality = ['M', 'm']
_midi_key = ['57', '59', '60', '62', '64', '65', '67']
_midi_quality = ['0 4 7','0 3 7']
_midi_accidental = [1, -1, 0]

# Interface
print("# Parsimonious Voice Leading")
print(f'## {date.today()}')
print(_key)
start_key = int(input("What note to start: "))
print(_accidental)
start_accidental = int(input("Flat or sharp: "))
print(_quality)
start_quality = int(input("What quality to start: "))
print(_key)
end_key = int(input("What note to end: "))
print(_accidental)
end_accidental = int(input("Flat or sharp: "))
print(_quality)
end_quality = int(input("What quality to end: "))
common = int(input("How many processes to keep in common between generations (1 or 2)?: "))

# Start and End Chords
start_midi_key = _midi_key[start_key]
start_midi_key = int(start_midi_key)
start_midi_chord = _midi_quality[start_quality].split(" ")
start_midi_chord = [eval(i) for i in start_midi_chord]
start_midi_chord = [x+start_midi_key for x in start_midi_chord]
start_midi_chord = [x+_midi_accidental[start_accidental] for x in start_midi_chord]
print(f'Start: {start_midi_chord}')
end_midi_key = _midi_key[end_key]
end_midi_key = int(end_midi_key)
end_midi_chord = _midi_quality[end_quality].split(" ")
end_midi_chord = [eval(i) for i in end_midi_chord]
end_midi_chord = [x+end_midi_key for x in end_midi_chord]
end_midi_chord = [x+_midi_accidental[end_accidental] for x in end_midi_chord]

# Packing the chords TODO: will always pack the chord because a 4th < 5th
if end_midi_chord[2] - end_midi_chord[0] > 6:
    end_midi_chord = end_midi_chord[1:] + end_midi_chord[:1]
    end_midi_chord[2] = end_midi_chord[2] + 12
    print(f'Packed End: {end_midi_chord}')
else:
    print(end_midi_chord)
exit()
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
    print(f'Change structProc {magicList}')
    for m in magicList:
        if m == 0 and a < onsetLength:
            a+=1
        elif m == 1 and b < continuationLength:
            b+=1
        elif m == 2 and c < terminationLength:
            c+=1
        elif a == onsetLength and b == continuationLength and c == terminationLength:
            print(end_key)
            print(end_accidental)
            print(end_quality)
            exit()
    else:
        pass
    print(onsetList[a])
    print(continuationList[b])
    print(terminationList[c])
