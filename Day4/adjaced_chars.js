// Day 4: Secure Container
// It is a six-digit number.
// The value is within the range given in your puzzle input.
// Two adjacent digits are the same (like 22 in 122345).
// Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
// Part2: the two adjacent matching digits are not part of a larger group of matching digits (there should be exactly 2)

const min = 206938
const max = 679128
let validPasscodes_part1 = []

const testForAdjancent = (number) => {
    const regExp = /(.)\1/
    return number.toString().match(regExp)
}

const testForDecrease = (number) => {
    let previousNumber = 9  //starting from biggest digit (in base10)
    let notDecreasing = 0
    const characters = number.toString().split("").reverse()
    
    characters.map(number => {
        if (previousNumber-number < 0)
            notDecreasing++
        previousNumber = number
    })

    if (notDecreasing == 0)
        return true
    else
        return false 
}

const testForMultipleAdjancent = (number) => {
    let previous = ""
    let adjacedCharsTemp = []
    let numberOfAdjaced = 0
    let result = false

    const characters = number.toString().split("")

    characters.map(char => {

        hasAdjaced = char == previous
        
        if (hasAdjaced) 
            adjacedCharsTemp.push(char)

        if (adjacedCharsTemp.length == 1) {
            result = true
        }

        if (adjacedCharsTemp.length > 1)
            result = false

        //empty list of adjaced characters if current charcter is not included in the adjaced chars
        if (!adjacedCharsTemp.includes(char)) {
            adjacedCharsTemp.length = 0

            // if there are exactly 2 adjaced characters (ie. result is true), increase counter for matches
            if (result == true)
                numberOfAdjaced++  
        }

        previous = char
    })
    
    if (numberOfAdjaced > 0 || result)
        return true
    else
        return false 
}

for (i=min; i <= max; i++) {
    if (testForDecrease(i) && testForAdjancent(i))
        validPasscodes_part1.push(i)
}

var listForPart2 = validPasscodes_part1.filter(item => testForMultipleAdjancent(item))

//1653
console.log(`Part1, number of valid passcodes: ${validPasscodes_part1.length}`)
//1133
console.log(`Part2, number of valid passcodes: ${listForPart2.length}`)