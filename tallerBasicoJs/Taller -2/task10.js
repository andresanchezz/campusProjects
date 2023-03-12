/* 10. Desarrolle un programa cíclico que capture un dato
numérico cada vez, y los vaya acumulando. El programa se
detiene cuando el usuario digita un cero. El programa debe
mostrar: LA SUMATORIA DE LOS VALORES, EL VALOR DEL
PROMEDIO, CUÁNTOS VALORES FUERON DIGITADOS, MAYOR
VALOR Y MENOR VALOR. */

let number
let numbers = []

do {
number = prompt('Enter a number')
numbers.push(number)
}while(number!== '0')
numbers = numbers.map(Number)
let plus = numbers.reduce((a,b)=> a + b, 0)
//Plus all numbers
console.log(`Plus numbers: ${plus}`)
//Average
numbers.pop()
let average = plus/numbers.length
console.log(`Average numbers: ${average}`)
//length
let lengthNumbers = numbers.length
console.log(`Quantity of numbers: ${lengthNumbers}`)
//Max
let maxNumber = Math.max(...numbers)
console.log(`Max number: ${maxNumber}`)
//Min
let minNumber = Math.min(...numbers)
console.log(`Min number: ${minNumber}`)