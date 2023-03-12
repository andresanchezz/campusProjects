/* 1. Construir el algoritmo para un programa que ingrese tres
notas de un alumno, si el promedio es menor o igual a 3.9
mostrar un mensaje "Estudie“, de lo contrario un mensaje que
diga "becado" */

let grades = 3
let data = []
let counter = 0
let finalGrade = 0
let msg = ''

function defineGrade(data){
    let dataAsInt = data.map(Number);
    finalGrade = dataAsInt.reduce((a,b)=> a + b, 0)
    finalGrade = finalGrade/3
    Math.round(finalGrade)
    console.log(finalGrade)
    alert(finalGrade <= 3.9 ? "Estudie" : "Becado")

}

function defineData(){
    do {
        gradesValue = prompt(`Enter grade ${counter+1}`)
        data.push(gradesValue)
        counter ++
        
        }while(counter < grades)
        console.log(data)
        defineGrade(data)
}

console.log(defineData())




