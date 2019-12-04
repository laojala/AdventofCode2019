// Day 4: Secure Container
// It is a six-digit number.
// The value is within the range given in your puzzle input.
// Two adjacent digits are the same (like 22 in 122345).
// Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

const min = 206938
const max = 679128
let validPasscodes = []

const testForAdjancent = (number) => {
    let previous = ""
    let numberOfAdjanced = 0
    const characters = number.toString().split("")

    characters.map(char => {
        hasAdjanced = char == previous
        previous = char
        if (hasAdjanced)
            numberOfAdjanced++
        })
    
    if (numberOfAdjanced > 0)
        return true
    else
        return false 
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

for (i=min; i <= max; i++) {
    if (testForDecrease(i) && testForAdjancent(i))
        validPasscodes.push(i)
}

console.log(`Valid codes: ${validPasscodes.length}`)



    