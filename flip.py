#!/usr/bin/python

"""
A simple coin flipping simulator I wrote based on the idea
that if you double up your bet after every loss, you will probably
gain in the long run.

Looks like this strategy ain't that great... Oh well

Author: undefined (Warren Hood)
"""

import random
import sys


INITIAL_CASH = int(input("Enter initial cash balance: ").strip())
INITIAL_BET = int(input("Enter min/initial bet: ").strip())
TARGET = int(input("Enter target cash: ").strip())

cash = INITIAL_CASH
verbose = "n" not in input("Verbose output?(Y/n) ").lower()

losses = 0
wins = 0


lastFlip = INITIAL_BET

flipCount = 0


def doFlip():
    global lastFlip, cash, INITIAL_BET, flipCount, verbose
    flipCount += 1
    if random.randint(0,1) == 1:
        cash += lastFlip
        lastFlip = INITIAL_BET
        if verbose:
            print("You won {:d}, new balance: {:d}".format(lastFlip, cash))
            print("Resetting to initial bet".format(lastFlip))
        return True
    else:
        cash -= lastFlip
        lastFlip *= 2
        if verbose:
            print("You lost {:d}, new balance: {:d}".format(lastFlip, cash))
            print("Doubling up bet to: {:d}".format(lastFlip))
        return False


print("Simulating...")

while 1:
    if cash >= TARGET or cash < lastFlip:
        if cash >= TARGET:
            wins += 1
            print("You made {:d} after {:d} flips".format(cash, flipCount))
        else:
            losses += 1
            print("Broke after {:d} flips".format(flipCount))


        if losses == 0:
            print("Target reached/Broke ratio: {:d}:{:d}".format(wins,losses))
        else:
            print("Target reached/Broke ratio: {:f}".format(float(wins)/losses))

            
        if "n" not in input("Retry?(Y/n)?"):
            flipCount = 0
            lastFlip = INITIAL_BET
            cash = INITIAL_CASH
        else:
            break
    doFlip()
    
