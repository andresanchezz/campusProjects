//Simple way that won't grow

let grade1 = prompt("Enter a grade 1")
let grade2 = prompt("Enter a grade 2")
let grade3 = prompt("Enter a grade 3")

console.log(grade1)
console.log(grade2)
console.log(grade3)


let plus = parseFloat(grade1)+parseFloat(grade2)+parseFloat(grade3) 
console.log(plus)
let finalGrade = plus/3

alert(finalGrade <= 3.9 ? "Estudie" : "Becado")
console.log(finalGrade)
