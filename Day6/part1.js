const fs = require('fs')
const planetMap = fs.readFileSync('./map.dat', 'utf-8').split('\n')

// Initialize array for planet map. KEY is orbiter, VALUE is planet/MOC for that orbiter
// Then map input data to the nodes array
const nodes = { 'COM': null }
planetMap.map(item => item.split(')'))
    .forEach(([parent, name]) => nodes[name]=parent)
    
// Input variable is value (planet/MOC) from node
const orbits = (orbiter) => 
    orbiter ? 1 + orbits(nodes[orbiter]) : 0
    
let part1 = Object.keys(nodes).reduce((total, nodeKey) => total + orbits(nodes[nodeKey]), 0)
console.log(part1)

//map1: 47
//map: 417916