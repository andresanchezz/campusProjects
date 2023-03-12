/* 6. Construir el algoritmo en Javascript para un programa
para cualquier cantidad de estudiantes que lea el nombre,
el sexo y la nota definitiva y halle al estudiante con la mayor
nota y al estudiante con la menor nota y cuantos eran
hombres y cuantos mujeres. */

student = []
counter = 0
students = 0
let grades = []
let maxGrade

students = prompt('How many students are you going to enter')

do {
    let name = prompt('Enter a name')
    let gender = prompt('Enter a gender (m/f)')
    let grade = prompt('Enter a grade ')
    student.push({ name: name, gender: gender, grade: grade })
    counter++


} while (counter < students)

function findGrades() {
    for (i = 0; i < student.length; i++) {
        grades.push(student[i].grade)
    }
    maxGrade = Math.max(...grades)
    grades = grades.map(Number);
    Number(maxGrade)

    //Min Grade
    minGrade = Math.min(...grades)

    return maxGrade, minGrade, grades
}

function getGender() {
    male = []
    female = []
    for ( i = 0; i < student.length; i++) {
        if(student[i].gender === "f"){
            female.push(student[i].gender)
        }else{
            male.push(student[i].gender)
        }
    }

    return male, female
}


function studentsGrade() {
    getGender()
    findGrades()
    let indexMaxGrade = grades.indexOf(maxGrade)
    let indexMinGrade = grades.indexOf(minGrade)
    let maxGradeStudent = student[indexMaxGrade].name
    let minGradeStudent = student[indexMinGrade].name
    let totalMale = male.length
    let totalFemale = female.length
    console.log(`Student best grade: ${maxGradeStudent}: ${maxGrade}`)
    console.log(`Student worst grade: ${minGradeStudent}: ${minGrade}`)
    console.log(`Total men ${totalMale}`)
    console.log(`Total women ${totalFemale}`)


}

console.log(studentsGrade())

