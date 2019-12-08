def callComputer(oppcode, pointer, value=0):
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

    return doOperation(oppcode, pointer, operation, digits, value)
    

def doOperation(oppcode, pointer, operation, modes=[0,0,0], value=0):

    stepcount = 0

    if operation == 99:
        return [operation, 0, None]
    
    #operations 1, 2, 7 and 8 parameter mode and stepcount
    if operation == 1 or operation == 2 or operation == 7 or operation == 8:
        stepcount = 4
        if modes[0] == 0:
            pointer1 = oppcode[pointer+1]
        else:
            pointer1 = pointer+1
        if modes[1] == 0:
            pointer2 = oppcode[pointer+2]
        else:
            pointer2 = pointer+2
        if modes[2] == 0:
            position = oppcode[pointer+3]   
        else:
            position = pointer+3

    #operations 3 and 4, parameter mode and stepcount
    if operation == 3 or operation == 4:
        stepcount = 2
        if modes[0] == 0:
            position = oppcode[pointer+1]
        else:
            position = pointer+1

    #operations 5 and 6, parameter mode and stepcount
    if operation == 5 or operation == 6:
        stepcount = 3
        if modes[0] == 0:
            pointer1 = oppcode[pointer+1]
        else:
            pointer1 = pointer+1
        if modes[1] == 0:
            pointer2 = oppcode[pointer+2]
        else:
            pointer2 = pointer+2

    #handle instruction:

    if operation == 1:
        result = oppcode[pointer1] + oppcode[pointer2]
        oppcode[position] = result
        return [None, pointer+stepcount, None]

    if operation == 2:
        result = oppcode[pointer1] * oppcode[pointer2]
        oppcode[position] = result
        return [None, pointer+stepcount, None]

    if operation == 3:
        oppcode[position] = value
        return [None, pointer+stepcount, None]

    if operation == 4:
        return [None, pointer+stepcount, oppcode[position]]
    
    #5: jump-if-true
    if operation == 5:
        if (oppcode[pointer1] != 0):
            newPointer = oppcode[pointer2]
            return [None, newPointer, None]
        else:
            return [None, pointer+stepcount, None]
    
    #6: jump-if-false
    if operation == 6:
        if (oppcode[pointer1] == 0):
            newPointer = oppcode[pointer2]
            return [None, newPointer, None]
        else:
            return [None, pointer+stepcount, None]
            
    #7: less-than
    if operation == 7:
        if oppcode[pointer1] < oppcode[pointer2]:
            oppcode[position] = 1
        else:
            oppcode[position] = 0
        return [None, pointer+stepcount, None]
    
    #8: equals
    if operation == 8:
        if oppcode[pointer1] == oppcode[pointer2]:
            oppcode[position] = 1
        else:
            oppcode[position] = 0
        return [None, pointer+stepcount, None]