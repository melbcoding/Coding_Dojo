const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'e5e3d6c49bmsh082c8414fbf0dc8p174f25jsn7bfbfd8a55c2',
		'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com'
	}
};

// function searchit(element){
//     console.log(element.innerText)
//     fetch(`https://wordsapiv1.p.rapidapi.com/words/${element.value}`, options)
// 	.then(response => response.json())
// 	.then(response => console.log(response))
// 	.catch(err => console.error(err));
// }

const search= document.getElementById('searchBar')
function searchit(element){
    display.innerHTML=""
    console.log(element.value)
    fetch(`https://wordsapiv1.p.rapidapi.com/words/${element.value}`, options)
	.then(response => response.json())
	.then(response => {
        console.log(response.results[0].definition)
        let newDefinition =  response.results[0].definition
        const display= document.getElementById('display')
        display.innerHTML = "<h3>Definition:<h3>"
        const ptag = document.createElement('p')
        const ptext = document.createTextNode(`${newDefinition}`)
        ptag.appendChild(ptext)
        display.appendChild(ptag)
    })
	.catch(err => console.error(err));
}

