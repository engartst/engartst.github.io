#!/usr/bin/env python3
"""
Create neighborhood names and then see if they exist in the Triangle, NC
"""
from googlesearch import search


__author__ = "Stewart Engart"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    with open('raleighFirst.txt', 'r') as file:
        first = file.read()
    with open('raleighSecond.txt', 'r') as file:
        second = file.read()

    combos = []
    first = first.split()
    second = second.split()

    for i in range(len(first)):
        for j in range(len(second)):
            combos.append(first[i]+" "+second[j])

    results = []

    for query in combos:
        results.append(search(query, num_results=1))

    #print(list(results))
    print(list(combos))


if __name__ == "__main__":
    main()
