"""
Program to make a smooth transition of structuring processes from
Smalley 1997
Stewart Engart, 20221229
with random motion and growth processes
with random behaviors
with random spectral space
"""

__author__ = "Stewart Engart"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import date
from datetime import datetime
import logzero
from logzero import logger
import json
import random
import os
import sys

def main():
    random.seed(1)
    day = os.path.splitext(sys.argv[1])[0]
    print(day)
    log_format = '%(message)s'
    formatter = logzero.LogFormatter(fmt=log_format)
    logzero.setup_default_logger(formatter=formatter)
    logzero.logfile(f"./log/{day}.md")

    # get the categories from the json file
    with open('structProcess.json') as fp:
        data = json.load(fp)
    with open('motionGrowth.json') as fp:
        motionList = json.load(fp)
    with open('behavior.json') as fp:
        behaviorList = json.load(fp)
    with open('specSpace.json') as fp:
        spaceList = json.load(fp)

    # logger.info all the stuff in the list
    def print_interface(a):
        print(a+": ")
        print(data[a])
        print("---")

    logger.info(f'# {day}')
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
    endOnsetIndex = int(input("End onset index: "))
    endOnset = data["Onset"][endOnsetIndex]
    endContinuationIndex = int(input("End continuation index: "))
    endContinuation = data["Continuation"][endContinuationIndex]
    endTerminationIndex = int(input("End termination index: "))
    endTermination = data["Termination"][endTerminationIndex]
    COMMON = int(input("How many processes to keep in common between generations (1 or 2)?: "))
    defi = input("Do you want definitions (y or n)?: ")
    logger.info(f'First Gesture: ')
    logger.info(f'- {startOnset}')
    logger.info(f'- {startContinuation}')
    logger.info(f'- {startTermination}')
    logger.info(f'- {random.choice(motionList["motion"])}')
    logger.info(f'- {random.choice(behaviorList["causality"])}')
    logger.info(f'- {random.choice(behaviorList["coordination"])}')
    logger.info(f'- {random.choice(behaviorList["dominance"])}')
    logger.info(f'- {random.choice(behaviorList["conflict"])}')
    logger.info(f'- {random.choice(spaceList["specSpace"])}')

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
        logger.info("---")

        # put it into a loop to so it can be flexible with how many strucProc stays
        # in common
        logger.info(f'Change structProc {magicList}')
        for m in magicList:
            if m == 0 and a < onsetLength:
                a+=1
            elif m == 1 and b < continuationLength:
                b+=1
            elif m == 2 and c < terminationLength:
                c+=1
            elif a == onsetLength and b == continuationLength and c == terminationLength:
                logger.info(f'- {endOnset}')
                logger.info(f'- {endContinuation}')
                logger.info(f'- {endTermination}')
                logger.info(f'- {motion}')
                logger.info(f'- {random.choice(behaviorList["causality"])}')
                logger.info(f'- {random.choice(behaviorList["coordination"])}')
                logger.info(f'- {random.choice(behaviorList["dominance"])}')
                logger.info(f'- {random.choice(behaviorList["conflict"])}')
                logger.info(f'- {random.choice(spaceList["specSpace"])}')

                if defi == 'y':
                    logger.info("")
                    logger.info("## DEFINITIONS")
                    logger.info("### ONSETS")
                    logger.info("")
                    logger.info("departure: the action of leaving, especially to start a journey")
                    logger.info("emergence: the process of coming into view or becoming exposed after being concealed")
                    logger.info("anacrusis: 'delta' but also one or more unstressed notes before the first bar line of a piece or passage")
                    logger.info("attack: an aggressive and violent action against a person or place")
                    logger.info("upbeat: an unaccented beat preceding an accented beat")
                    logger.info("downbeat: an accented beat, usually the first of the bar")
                    logger.info("### CONTINUATIONS")
                    logger.info("")
                    logger.info("passage: the act or process of moving through, under, over, or past something on the way from one place to another")
                    logger.info("transition: the process or a period of changing from one state or condition to another")
                    logger.info("prolongation: extension of the spatial length of something")
                    logger.info("maintanence:  process of maintaining or preserving someone or something")
                    logger.info("statement: the occurrence of a musical idea or motive within a composition")
                    logger.info("### TERMINATION")
                    logger.info("")
                    logger.info("arrival: the emergence or appearance of a new development, phenomenon, or product")
                    logger.info("disappearance: the process or fact of something ceasing to exist or be in use")
                    logger.info("closure: a sense of resolution or conclusion at the end of an artistic work")
                    logger.info("release: allow or enable to escape from confinement; set free")
                    logger.info("resolution: the passing of a discord into a concord during the course of changing harmony")
                    logger.info("plane: a level of existence, thought, or development")
                    logger.info("")
                    logger.info("### MOTION AND GROWTH")
                    logger.info("")
                    logger.info("#### UNI")
                    logger.info("")
                    logger.info("ascent: a climb or walk to the summit of a mountain or hill")
                    logger.info("plane: a level of existence, thought, or development")
                    logger.info("descent: an action of moving downward, dropping, or falling")
                    logger.info("")
                    logger.info("#### RECIPROCAL")
                    logger.info("")
                    logger.info("parabola: ")
                    logger.info("oscillation: movement back and forth at a regular speed")
                    logger.info("undulation: the action of moving smoothly up and down")
                    logger.info("")
                    logger.info("#### CYCLIC")
                    logger.info("")
                    logger.info("rotation: the action of rotating around an axis or center")
                    logger.info("spiral: winding in a continuous and gradually widening (or tightening) curve")
                    logger.info("spin: rapid turning or whirling motion")
                    logger.info("")
                    logger.info("#### CENTRIC")
                    logger.info("")
                    logger.info("vortex: a mass of whirling fluid or air, especially a whirlpool or whirlwind")
                    logger.info("pericentrality: arranged around a center")
                    logger.info("centrifugal motion: apparent outward force on a mass when it is rotated")
                    logger.info("")
                    logger.info("#### BI/MULTIDIRECTIONAL")
                    logger.info("")
                    logger.info("agglomeration: a mass or collection of things")
                    logger.info("dissipation: to spread thin or scatter and gradually vanish")
                    logger.info("dilation: the act or action of enlarging, expanding, or widening")
                    logger.info("contraction: to draw together so as to become diminished in size")
                    logger.info("divergence: a drawing apart (as of lines extending from a common center)")
                    logger.info("convergence: independent development of similar traits or features (as of body structure or behavior) in unrelated or distantly related species or lineages")
                    logger.info("exogeny: the origins of existence of self, or the identity of self, emanating from, or sustaining, outside the natural or influenced realm")
                    logger.info("endogeny: processes that originate from within a living system such as an organism, tissue, or cell")
                    logger.info("")
                    logger.info("### SPECTRAL SPACE")
                    logger.info("")
                    logger.info("canopy: above 5,000Hz")
                    logger.info("center: 300Hz and 5,000Hz")
                    logger.info("root: below 300Hz")
                else:
                    pass
                exit()
        else:
            pass
        logger.info(f'- {onsetList[a]}')
        logger.info(f'- {continuationList[b]}')
        logger.info(f'- {terminationList[c]}')
        logger.info(f'- {motion}')
        logger.info(f'- {random.choice(behaviorList["causality"])}')
        logger.info(f'- {random.choice(behaviorList["coordination"])}')
        logger.info(f'- {random.choice(behaviorList["dominance"])}')
        logger.info(f'- {random.choice(behaviorList["conflict"])}')
        logger.info(f'- {random.choice(spaceList["specSpace"])}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
