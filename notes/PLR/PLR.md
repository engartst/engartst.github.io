# PLR

## Transforms

- P
    + parallel
    + 0 4 7 - 0 3 7
    + 0 3 7 - 0 4 7
- L
    + l word
    + 0 4 7 - 11 4 7 (0 5 8 [-1]?)
    + 0 5 8 - 1 5 8 (0 4 7 [+1]?)
- R
    + relative
    + 0 4 7 - 0 4 9
    + 0 4 9 - 0 4 7

## Steps

1. Take input from user for first chord: AM, etc.
2. Take input from user for last chord: Cm, etc.
3. Take input from user for how many common notes held: 1 or 2
4. Look up in dict to get notes in packed form: AM: 0 4 9 and Cm: 0 3 7
    a. Make a dict with chords in packed form (or should all Majors and minors be treated the same with the distances from each other computed in the first step)
    b. CM = 0 4 7 and C#M = 0 4 7 [+1] with the extra being added when the +60 (middle C MIDI) is added?
5. Look up transforms
