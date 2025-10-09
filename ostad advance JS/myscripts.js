console.log("Advance Javascripts")
// Templates literals(python er f string er moto)

const age = 16;
const intro = `"i'm ${age} year old "`
console.log(intro)

// Destructuring ( array & objrcts)
// 1-> array 

const colors = ["red", "green", "blue"]

const [color1,color2] = colors // array distructure
console.log(color1)
console.log(color2)

// 2-> object

const persone = {
    name : "skd",
    result : "5.00"
}

// const name = persone.name
// console.log(name)

const {name, result} = persone
console.log(name)
console.log(result)

////////// spread / rest operator(...)
const favcolor =["blue", "black"]
const okcolor = [...favcolor, "pink", "gray"]
console.log(okcolor)


const persone1 = {
    name : "skd",
    result : "5.00"
}

const persone2 = {
    ...persone1,
    name : "dev"
}

console.log(persone2)

//// rest operator
function jogfol(a,b, ...numbers){
    console.log(a,b)
    console.log(numbers)
}
jogfol(10,20,30,40,50)


///////////////// callback function
function greeting(){
    console.log(" greeting function!!")
}

function boroektakaj(callback){
    console.log("start...")
    callback();
    console.log("end....")
}

boroektakaj(greeting)

/////////////////////// closure
function counter(){
    let count =0

    return function(){
        let age = 50
        console.log("age",age)
        age = age+10

        count++
        return count
    }
}

const newFunc = counter()
console.log(newFunc())
console.log(newFunc())
console.log(newFunc())
console.log(newFunc())

// age 50
// 1
// age 50
// 2
// age 50
// 3
// age 50
// 4

//////////  Asynchronous
console.log("Burger khabo!!")
console.log("chef banachhe")
setTimeout(function(){
    console.log("burger banano ses ...waiter serve")
},5000)

console.log("pizza khabo!!")
console.log("chef banachhe")
setTimeout(function(){
    console.log("pizza banano ses ...waiter serve")
},2000) 

// Burger khabo!!
// chef banachhe
// pizza khabo!!
// chef banachhe
// pizza banano ses ...waiter serve
// burger banano ses ...waiter serve

//////////  promise
// const  myPromise = new Promise(function(resolve, reject){
//     if (5>7){
//         resolve("its true!")
//     }
//     else{
//         reject("its not good") 
//     }
// })

function fetchUserInfo(userId){
    return new Promise(
        function(resolve, reject)
        {
            setTimeout(
                function()
                {
                    if (userId> 0)
                    {
                        resolve(
                            {
                                id: userId, 
                                name : "kumar"
                            })
                    }
                    else
                    {
                        reject("Invalid Id")
                    }
                }, 3 * 1000
            ); 
        }
    );
}

 console.log("started............")
fetchUserInfo(1)
    .then(
        function(user){
            console.log(user)
            return user.name // return na korle porer then undefine hoye jabe
        }
    )
    .then(
        function(xyz){
            console.log(xyz)
        }
    )
    .catch(
        function(msg){
            console.log(msg)
        }
    )
 console.log("end............") 



// console.log("hi")
// setTimeout(function(){
//     console.log("bye")
// },3 * 1000)


// function FUserinfo(userid)
// {
//     return new Promise(function(resolve, reject){
//         setTimeout(function(){
//             if (userid>0){
//                 resolve({id:userid, name:"Sadhon"})
//             }
//             else{
//                 reject("sorry wrong!!!")
//             }
//         },7 * 1000)
//     })
// }

// FUserinfo(3)
//     .then((result) => {
//         console.log(result)
//         return result.name
//     })
//     .then(function(name){
//         console.log(name)

//     })
//     .catch((err) => {
//         console.log(err)
//     });