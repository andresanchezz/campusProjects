/* 5. Construir el algoritmo que lea por teclado dos números,
si el primero es mayor al segundo informar su suma y
diferencia, en caso contrario, informar el producto y la
división del primero respecto al segundo. */

let n = parseFloat
let number1 = prompt('Enter number 1')
let number2 = prompt('Enter number 2')


function plus (){
    let total = n(number1)+n(number2)
    let difference = total-number2*2
    console.log(alert(`${number1} and ${number2} Plus: ${total}, Difference: ${difference}`))
}

function division(){    
    let product = number1%number2
    let division = number1/number2
    console.log(alert(`${number1} and ${number2} Product: ${product}, Division: ${division}`))
}

if(number1<number2){
    plus()
}else{
    division()
}








