from settings import pointer, oppcode
from intCom import doOperation

#Day2-Part2
def test1():

    oppcode1 = oppcode[:]
    pointer1 = pointer

    while True :
        returnCode = doOperation(oppcode1, pointer1, oppcode1[pointer1])
        
        pointer1 = pointer1+4
        
        if returnCode == 99:
            print("Part 1 result: Oppcode[0] is 3790645:", oppcode1[0]==3790645)
            break

###Day2-Part2
def test2():

    for x in range(0, 99):
        for y in range(0, 99):

            pointer2 = 0
            oppcode2 = oppcode[:]
            oppcode2[1] = x
            oppcode2[2] = y
            returnCode = 0

            while (returnCode != 99):
                returnCode = doOperation(oppcode2, pointer2, oppcode2[pointer2])
                pointer2 = pointer2 + 4
            
            if oppcode2[0] == 19690720:
                print("Part 2 result is 6577:", str(oppcode2[1])+str(oppcode2[2]) == "6577")
                break
test1()
test2()