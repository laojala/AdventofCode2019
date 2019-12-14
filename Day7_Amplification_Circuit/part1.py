import sys
sys.path.append('../IntcodeComputer')
from settings import oppcodeDay7
from intcodeComputer import callComputer

from itertools import permutations

inputs = [0,1,2,3,4]
phases = permutations(inputs, 5)
results = []

for phase in phases:

    previousOutput = 0

    for amplifier in phase:
        pointer = 0
        returnCode = [None, pointer, None]
        oppcode = oppcodeDay7[:]
        firstRun = True

        while (returnCode[0] != 99):
            if (firstRun):
                returnCode = callComputer(oppcode, pointer, amplifier)
                pointer = returnCode[1]
                firstRun = False
            
            else:
                returnCode = callComputer(oppcode, pointer, previousOutput)
                pointer = returnCode[1]
            if (returnCode[2] or returnCode[2] == 0):
                previousOutput = returnCode[2]
        
    results.append(previousOutput)
            
#225056
print("Output is 225056:"), max(results) == 225056