var like_array= [9,12,9]

// checking to see if the liked_count.innerText is working
// iterate through array until span_id matches the value at that index
// compare current array index to the span_id passed through
// store increased value into a new variable
// replace innerText of span with new value 

function like(span_id){
    var liked_count= document.getElementById(span_id)
    console.log(liked_count.innerText, "this is the innerText")
    for(var i= 0; i<like_array.length; i++){
        if(like_array[i] == liked_count.innerText){
            var increase= parseInt(liked_count.innerText)
            increase++
            liked_count.innerText = increase
            like_array[i]= increase
        }

    }
}