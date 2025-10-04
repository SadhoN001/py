console.log("DOM")

// const item = document.getElementById('heading3')
// console.log(item)
// const item = document.querySelector('#heading3')
// console.log(item)
// const item = document.querySelector('h3')
// console.log(item)
// const item = document.querySelectorAll('h3')
// console.log(item)

// const h3element = document.querySelector("p")
// console.log(h3element)

// h3element.textContent = "Bye Bye"
// console.log(h3element.textContent)// Bye Bye

// h3element.innerHTML = "<i ><strong > NO NO </strong></i>"
// console.log(h3element.textContent)// NO NO

// // // p---> gpa

//Event 
//Event Listener 

// const text_me =() =>{
//     console.log("click hoise")
// }

// document.addEventListener("click", text_me)

// const bel = document.querySelector("button");

// bel.addEventListener("click", text_me); // function most use 

// bel.addEventListener("click", () =>{ // array functopm
//     console.log("click hoise")
// });
// bel.addEventListener("click", function(){ // anynemous function 
//     console.log("click hoise")
// });

let n= 1;
const text_me =() =>{
    console.log("click hoise")
    const pel = document.querySelector("p")
    pel.textContent = "GPA : 5.0 and click-> "+n,
    n=n+1;

}
const bel = document.querySelector("button");
bel.addEventListener("click", text_me);

////// setTimeout() and setInterval()

const say_hello = () =>{
    console.log("hellooooooooooo")
}

say_hello()
const tid= setTimeout(say_hello, 2 * 1000)
// setInterval(say_hello, 2 * 1000) 

// clearTimeout(tid)