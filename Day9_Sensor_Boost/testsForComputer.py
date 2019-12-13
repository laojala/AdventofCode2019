from settings import pointer, oppcode, oppcodeDay5
from intcodeComputer import callComputer


#Day2-Part2
def test1():
    returnCode = [0, None, None]
    oppcode1 = oppcode[:]
    pointer1 = pointer
    #returnCode[0] = 0

    while (returnCode[0] != 99):
        returnCode = callComputer(oppcode1, pointer1)
        
        if returnCode[0] == 99:
            print("Part 1 result: Oppcode[0] is 3790645:"), oppcode1[0]==3790645
        else:
            pointer1 = returnCode[1]

###Day2-Part2
def test2():

    for x in range(0, 99):
        for y in range(0, 99):
            returnCode = [0, None, None]
            pointer2 = pointer
            oppcode2 = oppcode[:]
            oppcode2[1] = x
            oppcode2[2] = y

            while (returnCode[0] != 99):
                returnCode = callComputer(oppcode2, pointer2)
                if (returnCode[0] != 99):
                    pointer2 = returnCode[1]
            
            if oppcode2[0] == 19690720:
                print("Part 2 result is 6577:"), str(oppcode2[1])+str(oppcode2[2]) == "6577"
                break

def test3():
    oppcode3 = [1002,4,3,4,33]
    pointer = 0
    returnCode = [0, 0, None]

    while (returnCode[0] != 99):
        returnCode = callComputer(oppcode3, pointer)
        pointer = returnCode[1]
    
    print("Test 3, Return code is 99:"), returnCode[0] == 99

def test4():
    oppcode4 = [3,0,4,0,99]
    pointer = 0
    returnCode = [0, 0, None]
    inputCode = 123
    results = []

    while (returnCode[0] != 99):
        returnCode = callComputer(oppcode4, pointer, inputCode)
        pointer = returnCode[1]
        if returnCode[2]:
            results.append(returnCode[2])

    print("Test 4, Output value is 123:"), results[0] == 123

# Day 5 - Part1
def test5():

    oppcode5 = oppcodeDay5[:]
    pointer = 0
    returnCode = [0, 0, None]
    inputCode = 1
    results = []

    while (returnCode[0] != 99):
        returnCode = callComputer(oppcode5, pointer, inputCode)
        pointer = returnCode[1]
        if returnCode[2]:
            results.append(returnCode[2])

    print("Test 5: Return code is 5821753:"), results[-1] == 5821753


test1()
test2()
test3()
test4()
test5()