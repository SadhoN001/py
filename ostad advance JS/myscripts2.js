const todoListEl = document.querySelector("#todo-list")
// console.log(todoListEl);

fetch("https://jsonplaceholder.typicode.com/todos/")
// .then(async(response)=>{
//     // console.log(response);
//     console.log(await response.json());
    
// })
.then((response)=>{
    return response.json()
})
.then((data)=>{
    console.log(data)
    // console.log(data[0])
    // console.log(data[0].title)
    finalHTML = ""
    for(item of data){
        finalHTML += `<li>${item.title}</li>`
    }

    // console.log(finalHTML)
    todoListEl.innerHTML = finalHTML
})

////////////// POST

// const todoData = {
//     userId : 1,
//     "id": 1,
//     "title": "niramish khabo",
//     "completed": false
// }

// fetch("https://jsonplaceholder.typicode.com/todos/", {
//     method: "POST",
//     headers : {
//         "content-type" : "application/json"
//     },
//     body : JSON.stringify(todoData)
// })
// .then((response)=> response.json())
// .then((data)=>{
//     console.log(data)
// })
// .catch(err=>{
//     console.log(err);
    
// })

/////// form handling
const todoFormEl = document.querySelector("#todoForm")
console.log(todoFormEl);

todoFormEl.addEventListener("submit", (event)=>{
    event.preventDefault();// reload hobe na submit e

    // console.log(event.target)    
    // console.log(event.target.todo)
    // console.log(event.target.todo.value) 

    const todoTitle = event.target.todo.value;

    const todoData = {
        userId : 1,
        "id": 1,
        "title": todoTitle,
        "completed": false
    }

    fetch("https://jsonplaceholder.typicode.com/todos/", {
        method: "POST",
        headers : {
            "content-type" : "application/json"
        },
        body : JSON.stringify(todoData)
    })
    .then((response)=> response.json())
    .then((data)=>{
        console.log(data)
        
        event.target.todo.value = ""
    })
    .catch(err=>{
        console.log(err);
        
    })
}) 