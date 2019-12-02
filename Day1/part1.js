const fs = require('fs')

const spacecrafts = fs.readFileSync('./Space_Vessels.txt', 'utf-8').split('\n')

const fuelNeed = (mass) =>
    Math.floor(mass/3) - 2

const totalFuelNeed = (list) => 
    list.reduce((sum, mass) => sum + fuelNeed(mass), 0)

console.log("Total Fuel Need: " + totalFuelNeed(spacecrafts))