// to run: install node.js, and then in terminal: node part1.js

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

console.log(`Result is 1584: ${part1_checksum() === 1584}`)