from settings import oppcodeDay5
from intcodeComputer import callComputer

oppcode = oppcodeDay5[:]
inputCode = 5
pointer = 0
returnCode = [0, None, None]
results = []

while (returnCode[0] != 99):
    returnCode = callComputer(oppcode, pointer, inputCode)
    pointer = returnCode[1]
    if returnCode[2] or returnCode[2] == 0:
        results.append(returnCode[2])

#11956381
print("Return code:", results)
