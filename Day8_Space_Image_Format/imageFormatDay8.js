const fs = require('fs')
const data = fs.readFileSync('./input.dat', 'utf-8').split('')
const width = 25
const height = 6

const image = data.map(item => Number(item))
const layeredData = []
while (image.length) {
    layeredData.push(image.splice(0, width*height))
}

const part1_checksum = () => {
    let numberOfZeroDigits = layeredData[0].length
    const fewestZeroDigits = []

    layeredData.forEach(layer => {
        let lenghtOfCurrent = layer.filter(digit => digit === 0).length
        if (lenghtOfCurrent < numberOfZeroDigits) {
            numberOfZeroDigits = lenghtOfCurrent
            fewestZeroDigits.pop()
            fewestZeroDigits.push(layer)
        }
    })
    return fewestZeroDigits[0].filter(digit => digit === 1).length * fewestZeroDigits[0].filter(digit => digit === 2).length
} //part1_checksum

console.log(`Part 1 result is 1584: ${part1_checksum() === 1584}`)


//part2
const part2_decode = () => {

    const getColor = (arrayOfArrays, index) => 
        arrayOfArrays.find(array => {
            if (array[index] === 0 || array[index] === 1)
                return array
    })

    //create transparent Array
    const transparent = new Array(width*height)
    transparent.fill(2)

    //filling just created transparent array
    const finalImage = transparent.map((item, index) => {
        let array = getColor(layeredData, index)
        if (array)
            return array[index]
        else 
            return item
    })

    const toBePrinted = []

    while (finalImage.length) 
        toBePrinted.push(finalImage.splice(0, 25))
    
    toBePrinted.forEach(row => {
        temp = []
        row.forEach(char => {
            if (char === 0)
                temp.push(" ")
            else
                temp.push("█")
        })
        console.log(temp.join(''))
    })
}

part2_decode()
