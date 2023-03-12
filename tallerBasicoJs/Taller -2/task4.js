/* 4. Construir el algoritmo que solicite el nombre y edad de 3
personas y determine el nombre de la persona con mayor edad. */


let names = []
let ages = []
let counter = 0
do{
    let name = prompt('Enter a name')
    names.push(name)
    let age = prompt('Enter an age ')
    ages.push(age)
    counter ++
}while(counter<3)

function getOlder(){
    let older = Math.max(...ages)
    let agesInt = ages.map(Number);
    let indexAges = agesInt.indexOf(older)
    console.log(ages)
    console.log(indexAges)
    alert(`Older person: ${names[indexAges]}: ${older} years`)
}

console.log(getOlder())




