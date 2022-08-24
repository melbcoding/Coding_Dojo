const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'e5e3d6c49bmsh082c8414fbf0dc8p174f25jsn7bfbfd8a55c2',
		'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com'
    }
}


function searchAPI(element){
    console.log(element.value)
    const userInput = element.value
    fetch(`https://wordsapiv1.p.rapidapi.com/words/${userInput}`, options)
    .then(response=>response.json())
    // .then(response => console.log(response))
    .then(response => {
        console.log(response);

        const displayDiv= document.getElementById("displayResult")
        // definition
        const resDefinition= response.results[0].definition
        const ptag= document.createElement('p')
        const ptext = document.createTextNode(`${resDefinition}`)

        // syllables

        const resSyllable= response.syllables.list
        const syllableSpan = document.createElement('span')
        syllableSpan.innerText = ""
        for(let i=0; i<resSyllable.length; i++){
            console.log(resSyllable[i])
            const spanText= `${resSyllable[i]}`
            syllableSpan.innerText += ` ${spanText}`
        }

        ptag.appendChild(ptext)
        console.log(syllableSpan)
        displayDiv.append(syllableSpan, ptag)
        // displayDiv.innerHTML = `<h3> Definition</h3>`
        // displayDiv.appendChild(ptag)
        })
}