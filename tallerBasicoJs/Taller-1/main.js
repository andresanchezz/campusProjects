let recommendations =  ['Exceeds proficiency','Demonstrates proficiency', 'Approaches proficiency'
,'Falls well below proficiency', 'Lacks all proficiency', 'No attempt made']
let grade = prompt('Enter a grade between 0 and 100')
let letter = ''
let recommendation = ''

function transform(grade){
    if(grade > 100 || grade < 0){
        letter='Invalid grade',
        recommendation='Invalid grade'
    }else if(grade >= 90 && grade <= 100){
        letter = 'A'
        recommendation = recommendations[0]
    }else if(grade >= 80 && grade <= 89){
        letter = 'B'
        recommendation = recommendations[1]
    }else if(grade >= 70 && grade <= 79){
        letter = 'C'
        recommendation = recommendations[2]
    }else if(grade >= 60 && grade <= 69){
        letter = 'D'
        recommendation = recommendations[3]
    }else if(grade < 60 && grade >= 1){
        letter = 'E'
        recommendation = recommendations[4]
    }else if(grade == 0){
        letter = 'Z'
        recommendation = recommendations[5]
    }

    return recommendation, letter
}

transform(grade)

let html = "";
const selector = document.querySelector("#app");


html += `
<div class="container mt-2 ">
<div class="row mt-4">
    <div class="col-lg-6 col-md-12">
        <h1 class="mb-3 text-danger">SBG Scale converter</h1>
        <h3>Your grade was: <span class="text-danger">${grade}</span></h3>
        <h3>Your grade in SBG is: <span class="text-danger">${letter}</span></h3>
        <h3>A note:
            <br>
            <span class="text-danger">${recommendation}</span>
        </h3>
    </div>
    <div class="col-lg-6 col-md-12">
        <img src="tableScores.png" alt="if u cant see this img is the SBG-scores table" class="img-fluid mt-2">
    </div>
</div>
</div>
`

selector.innerHTML = html