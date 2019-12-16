basePattern = [0, 1, 0, -1]
input = []
patterns = []


with open("input.dat") as fileObj: 
    for line in fileObj:  
        for char in line:
            input.append(char)

def createPattern(position, length):
    pattern = []
    for item in range(length):
        if len(pattern) > length+1:
            break
        for value in basePattern:
            if len(pattern) > length+1:
                break
            numberOfOccurences = position+1
            while numberOfOccurences > 0:
                if len(pattern) > length+1:
                    break
                pattern.append(value)
                numberOfOccurences += -1
    pattern.pop(0)
    return pattern[0:length]

#create base pattern 
for idx, item in enumerate(input):
    patterns.append(createPattern(idx, len(input)))

for n in range(100):
    signal= []
    for pattern in patterns:
        result = 0
        for idx, item in enumerate(pattern):
            result += item * int(input[idx])
        signal.append(int(str(result)[-1]))   
    input = ''.join(map(str, signal))

#first eight digits: 96136976
print(input)

#note: algorithm is very unoptimal and slow... need to find out how to make it faster