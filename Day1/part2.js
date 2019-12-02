const fs = require('fs')

const spacecrafts = fs.readFileSync('./Space_Vessels.txt', 'utf-8').split('\n')

const fuelNeed = (mass) => {
    let fuelNow = Math.floor(mass/3) - 2
    return fuelNow > 0 ? fuelNow + fuelNeed(fuelNow) : 0
}

const totalFuelNeed = (list) => 
    list.reduce((sum, mass) => sum + fuelNeed(mass), 0)

console.log("Total Fuel Need (including extra fuel): " + totalFuelNeed(spacecrafts))