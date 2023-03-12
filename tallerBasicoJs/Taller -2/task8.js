/* 8. Programa que Ingrese por teclado:
a. el valor del lado de un cuadrado para mostrar por pantalla el
perímetro del mismo
b. la base y la altura de un rectángulo para mostrar el área del
mismo */

let square = prompt('Value of a side of square ')
let perimeter = square*4

let base = prompt('Value of a base of a rectangle')
let height = prompt('Value of a height of a rectangle')
let area = (base*height)/2

alert(`Perimeter square ${perimeter}`)
alert(`area rectangle ${area}`)

