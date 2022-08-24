window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});

// // function logout(unicorn){
// //     if(unicorn){
// //     document.getElementById("login").innerHTML = "logout";
// //     console.log("success!")
// //     }
// //     else{
// //     console.log("something is wrong with the function")
// //     }
// // }

// // Anatomy of Javascript
// // functional programming
// var x = 5
// // define a function with the name and optional parameter
// // functions may accept arguments
// function myfunction(parameter){
//     // now we are inside the function
//     // var check_param = parameter
//     // console.log prints/shows data where it is presently 
//     console.log(parameter)
//     // return moves data from one place to another
//     return parameter + 1 

// }

// // call the function
// myfunction(7) 
// // console.log calls function will print what is inside and then print what it is returning. The return is literally being passed to this first console.log
// console.log(myfunction(5))

// var call_function = myfunction(5)
// console.log(call_function)



// basic anatomy of a javascript 
// 
// function myfunction(parameters){
//     // now inside the function

// }
// // on the html element you have an event attribute
// // we place an event attribute on an html element to activate javascript functions
// onclick= "myfunction(argument)"
// onmouseover, onmouseout, onchange

// function search(data){
    // add function for searching an api 
    // appendChild add results to the lower part of the DOM
// }

// create a button click event
//  that increases the number of likes on the innerHTML of a ptag

function likes(param){
    console.log("you are in ")
    // grab the likeCount.innerText and store it in a new variable for later use
    var count = document.getElementById("likeCount").innerText
    // est the innerText as an integer in order to increase
    var current_count= parseInt(count)
    // check to see if this is working
    console.log(current_count + " is this working?")
    // adding to the integer version I've created
    var increase = current_count + 1
    console.log(`this has increased? ${increase}`)
    // reassign the innerText of likeCount with the updated amount
    document.getElementById("likeCount").innerText = increase

}

