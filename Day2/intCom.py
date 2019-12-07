def doOperation(oppcode, pointer, operation):

    if operation == 99:
        return 99
    
    pointer1 = oppcode[pointer+1]
    pointer2 = oppcode[pointer+2]
    position = oppcode[pointer+3]

    if operation == 1:
        result = oppcode[pointer1] + oppcode[pointer2]
        oppcode[position] = result
        return 1

    if operation == 2:
        result = oppcode[pointer1] * oppcode[pointer2]
        oppcode[position] = result
        return 2
