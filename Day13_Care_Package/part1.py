import sys
sys.path.append('../IntcodeComputer')
from settings import oppcodeDay13
from intcodeComputer import callComputer, setMemory

oppcode = oppcodeDay13[:]
inputCode = 0
pointer = 0
relativebase = 0
returnCode = [pointer, None, None, relativebase]
results = []

outputSequence = []

setMemory(oppcode)

while (returnCode[0] != 99):
    returnCode = callComputer(oppcode, pointer, inputCode, relativebase)
    pointer = returnCode[1]
    if returnCode[3] or returnCode[3] == 0:
        relativebase = returnCode[3]
    
    if returnCode[2] or returnCode[2] == 0:
        if len(outputSequence) < 2:
            outputSequence.append(returnCode[2])
        else:
            outputSequence.append(returnCode[2])
            results.append(outputSequence)
            outputSequence = []


numberOfBlockTiles = 0

for sequence in results:
    if sequence[2] == 2:
        numberOfBlockTiles += 1

print("Number or block tiles (2):"), numberOfBlockTiles

