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
        return [99, 0, None]
    
    ##operations 1 and 2, parameter mode and stepcount
    if operation == 1 or operation == 2:
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

    ##operations 3 and 4, parameter mode and stepcount
    if operation == 3 or operation == 4:
        stepcount = 2
        if modes[0] == 0:
            position = oppcode[pointer+1]
        else:
            position = pointer+1

    #handle instruction:

    if operation == 1:
        result = oppcode[pointer1] + oppcode[pointer2]
        oppcode[position] = result
        return [1, stepcount, None]

    if operation == 2:
        result = oppcode[pointer1] * oppcode[pointer2]
        oppcode[position] = result
        return [2, stepcount, None]

    if operation == 3:
        oppcode[position] = value
        return [3, stepcount, None]

    if operation == 4:
        return [4, stepcount, oppcode[position]]