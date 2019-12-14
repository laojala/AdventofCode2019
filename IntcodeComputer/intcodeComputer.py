
# adds memory slots to oppcode. Size of the memory is 3 times the length of the initial oppcode
def setMemory(oppcode):
    for x in range (len(oppcode), len(oppcode)*100):
        oppcode.append(0)


def callComputer(oppcode, pointer, inputValue=0, relativebase=0):
    instruction = oppcode[pointer]
 
    # put instruction as list of digits and then reverse it
    digits = [int(d) for d in str(instruction)]
    digits.reverse()

    #pad insturctions list with zeros, if lenght is less than 5
    while(len(digits) < 5):
        digits.append(0)
    
    # pop 2 first digits from initial list
    # if second popped digit is 0, omit it
    firstDigit = digits.pop(0)
    secondDigit = digits.pop(0)
    if secondDigit == 0:
        secondDigit = ""

    # combine 2 first digits to get operation
    operation = operation=int(str(firstDigit) + str(secondDigit))
    # rest of the list is now modes

    return doOperation(oppcode, pointer, operation, digits, inputValue, relativebase)
    

def doOperation(oppcode, pointer, operation, modes=[0,0,0], value=0, relativebase=0):

    stepcount = 0

    if operation == 99:
        return [operation, 0, None, relativebase]

     #operations 1, 2, 7 and 8 parameter mode and stepcount
    if operation == 1 or operation == 2 or operation == 7 or operation == 8:
        stepcount = 4
        if modes[0] == 0:
            pointer1 = oppcode[pointer+1]
        elif modes[0] == 1:
            pointer1 = pointer+1
        elif modes[0] == 2:
            pointer1 = relativebase+oppcode[pointer+1]

        if modes[1] == 0:
            pointer2 = oppcode[pointer+2]
        elif modes[1] == 1:
            pointer2 = pointer+2
        elif modes[1] == 2:
            pointer2 = relativebase+oppcode[pointer+2]

        if modes[2] == 0:
            position = oppcode[pointer+3]   
        elif modes[2] == 1:
            position = pointer+3
        elif modes[2] == 2:
            position = relativebase+oppcode[pointer+3]

    #operations 3,4, 9 parameter mode and stepcount
    if operation == 3 or operation == 4  or operation == 9:
        stepcount = 2
        if modes[0] == 0:
            position = oppcode[pointer+1]
        elif modes[0] == 1:
            position = pointer+1
        elif modes[0] == 2:
            position = relativebase+oppcode[pointer+1]

    #operations 5 and 6 parameter mode and stepcount
    if operation == 5 or operation == 6:
        stepcount = 3
        if modes[0] == 0:
            pointer1 = oppcode[pointer+1]
        elif modes[0] == 1:
            pointer1 = pointer+1
        elif modes[0] == 2:
            pointer1 = relativebase+oppcode[pointer+1]

        if modes[1] == 0:
            pointer2 = oppcode[pointer+2]
        elif modes[1] == 1:
            pointer2 = pointer+2
        elif modes[1] == 2:
            pointer2 = relativebase+oppcode[pointer+2]

    #handle instruction. Content of output: ["99 exit code", "new pointer", "output value", relativebase]

    if operation == 1:
        result = oppcode[pointer1] + oppcode[pointer2]
        oppcode[position] = result
        return [None, pointer+stepcount, None, relativebase]

    if operation == 2:
        result = oppcode[pointer1] * oppcode[pointer2]
        oppcode[position] = result
        return [None, pointer+stepcount, None, relativebase]

    #3: input
    if operation == 3:
        oppcode[position] = value
        return [None, pointer+stepcount, None, relativebase]
    
    #4: output
    if operation == 4:
        return [None, pointer+stepcount, oppcode[position], relativebase]
    
    #5: jump-if-true
    if operation == 5:
        if (oppcode[pointer1] != 0):
            newPointer = oppcode[pointer2]
            return [None, newPointer, None, relativebase]
        else:
            return [None, pointer+stepcount, None, relativebase]
    
    #6: jump-if-false
    if operation == 6:
        if (oppcode[pointer1] == 0):
            newPointer = oppcode[pointer2]
            return [None, newPointer, None, relativebase]
        else:
            return [None, pointer+stepcount, None, relativebase]
            
    #7: less-than
    if operation == 7:
        if oppcode[pointer1] < oppcode[pointer2]:
            oppcode[position] = 1
        else:
            oppcode[position] = 0
        return [None, pointer+stepcount, None, relativebase]
    
    #8: equals
    if operation == 8:
        if oppcode[pointer1] == oppcode[pointer2]:
            oppcode[position] = 1
        else:
            oppcode[position] = 0
        return [None, pointer+stepcount, None, relativebase]

    #9: set relative base
    if operation == 9: 
        newBase = relativebase+oppcode[position]
        return [None, pointer+stepcount, None, newBase]
