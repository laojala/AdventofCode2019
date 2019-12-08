from settings import oppcodeDay5
from intcodeComputer import callComputer

oppcode = oppcodeDay5[:]
pointer = 0
returnCode = [0, 0, None]
inputCode = 1
results = []

while (returnCode[0] != 99):
    returnCode = callComputer(oppcode, pointer, inputCode)
    pointer = pointer + returnCode[1]
    if returnCode[2]:
        results.append(returnCode[2])

print("Return code: "), results