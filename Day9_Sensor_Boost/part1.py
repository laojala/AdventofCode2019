import sys
sys.path.append('../IntcodeComputer')
from settings import oppcodeDay9
from intcodeComputer import callComputer, setMemory

oppcode = oppcodeDay9[:]
inputCode = 2
pointer = 0
relativebase=0
returnCode = [pointer, None, None, relativebase]
results = []

setMemory(oppcode)

while (returnCode[0] != 99):
    returnCode = callComputer(oppcode, pointer, inputCode, relativebase)
    pointer = returnCode[1]
    if returnCode[3] or returnCode[3] == 0:
        relativebase = returnCode[3]
    if returnCode[2] or returnCode[2] == 0:
        results.append(returnCode[2])

print("Output:"), results