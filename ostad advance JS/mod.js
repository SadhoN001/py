// ////// scope 3 type (global, function, block)

// // global scope
// let name = "Alex"

// function sayHello(){
//     console.log("hello "+ name);
// }
// sayHello()

// // functional scope
// function greet(){
//     let msg = "Goood Morning"
//     console.log(msg)
// }
// greet()

// // Block scope (let, const)
// if (true){
//     let age = 25
//     console.log(age)
// }

// // console.log(age)
// ////// Lexical Environment

// function outer(){
//     let name = "bangladesh"

//     function inner(){
//         console.log(name)
//     }
//     inner()
// }

// outer()

// ////// clousers 
//  function outerFunction(){
//     let counter = 0

//     function innerFunction(){
//         counter++;
//         console.log("counter is "+ counter);
//     }
//     return innerFunction
//  }

//  const mycounter = outerFunction()
//  mycounter()
//  mycounter()
//  mycounter()
//  mycounter()

//  //////////////////// OOP 
//  //// Encapsulation - ডাটা এবং মেথড ফাংশন একসাথে প্যাক করে রাখে
//  //// Abstruction - অপ্রয়োজনীয় তথ্য লুকানো 
//  //// Inheritance - একটি ক্লাস আরেকটি ক্লাসের বৈশিষ্ট্য (property / method) ব্যবহার করে 
//  //// Polymorphism - ovverriding,overloading

// class MyClass{
//     constructor(){
//         console.log("constructor call")
//     }

//     x=50;
//     myfun() // Method
//     {
//         console.log("hello js oop")
//     }
// }

// let myobj = new MyClass()
// myobj.myfun()
 
class Student{
    constructor(name, roll){
        this.name = name;
        this.roll = roll;

        console.log(name, roll);
    }

    myFun() // Method 
    {
        console.log(this.name);
    }
}


const st1 = new Student("alex", 20)
const st2 = new Student("raj", 50)

st1.myFun()
console.log(st2.name);

// static

class MyClass{
    static hello(){
        console.log("OOP Static")
    }
}

MyClass.hello()

//// inheritance

// class Parent{
//     hello(){
//         console.log("this is parent");
//     }
// }

// class child extends Parent{
    
// }

// let chilOb = new child()

// chilOb.hello()

//// overloading support kore na 
//// overriding

// class Parent{
//     hello(){
//         console.log("this is parent");
//     }
// }

// class child extends Parent{
//     hello(){
//         console.log("this is child");
//     }
// }

// let chilObj = new child()

// chilObj.hello()

//// super keyword 
// class Parent{
//     hello(){
//         console.log("this is parent");
//     }
// }

// class child extends Parent{
//    test(){
//     super.hello()
//    }
// }

// let chilObj = new child()  

// chilObj.test()

////// arrow function vs regular function 

// regular function :
function add(a,b){
    return a+b
}
console.log(add(1,2));

// arrow function:
let addition = (a,b)=>{
    return a+b
}
console.log(addition(2,2)); 

////// Hosting - func and variable upore jay ..js nijer matchine er modhhe eivabe kore
console.log(name);
var name = "olaaala"

hello()

function hello(){
    console.log("hello from hosting")
}

////// Promis and Async

// const getData = ()=>{
//     return new Promise((resolve, reject)=>{
//         const success = true

//         setTimeout(()=>{
//             if(success){
//                 resolve("data pass success")
//             }
//             else{
//                 reject("data pass failed")
//             }
//         },2000)
//     })
// }

// getData()
//     .then((result)=>{
//         console.log(result);
        
//     })
//     .catch((error)=>{
//         console.log(error);
//     })

// console.log("project running...");


//// Async 

// const fetchData =async()=>{
//     try{
//         const response = await fetch("https://jsonplaceholder.typicode.com/users/1")
//         const user = await response.json()
//         console.log(user);
        
//     }
//     catch(error){
//         console.log("error was --> "+    error);
        
//     }
// }

// fetchData()

////// Error Handling - try, catch, finally 

try{
    let taka = "2000hi"
    console.log(typeof(taka));
    let balance = Number(taka)

    if(isNaN(balance)){
        throw new Error("invalid input")
    }
    console.log("your balance is "+balance)
}
catch(error){
    console.log("This error is --> "+error);
    console.log("This error is --> "+error.message);

}
finally{
    console.log("This is final block");
    
}


////// Javascript Module (ES6 import / Export  )
//// html script e type ="module" dite hobe

import {jog , biyog} from "./math.js"

console.log(jog(5,5));
console.log(biyog(5,5));

import gun from "./math.js"
console.log(gun(3,3));

////// Destructuring(array , object)

const student = ["rahim", 22, "dhaka"];

// const name = student[0];
// const age = student[1];
// const city = student[2];
const [st_name, age, city] = student;
console.log(`name: ${st_name}, Age: ${age}, city: ${city}`);

const persone = {
    us_name : "skd",
    result : "5.00"
}

// const name = persone.name
// console.log(name)
const {us_name, result} = persone
console.log(us_name)
console.log(result)

////// spread / rest operator(...)
//spread
const a1= [1,2]
const a2 =[3,4]
const marge = [...a1, ...a2]
console.log(marge);

//rest
function MyArr(...arry){
    console.log(arry);
}
let arr1 = [1,2,3]
let arr2 = [4,5,6]
let arr3 = [7,8,9]

MyArr(arr1,arr2,arr3)

////// Fetch API and Async data Handling 
//// Fetch

// fetch("https://jsonplaceholder.typicode.com/posts")
// .then((response)=> response.json()) // convert to json
// .then((data)=>{
//     console.log(data); // get data in console
// })
// .catch((error)=>{
//     console.log(error);
// })

////// Async *****

// async function getData(){
//     try {
//         let response = await fetch("https://jsonplaceholder.typicode.com/posts")
//         let data = await response.json()

//         console.log((data));
        
//     } catch (error) {
//         console.log(error);
//     }
// }

// getData()

////// Web Storage (localStorage, sessionStorage)
// data set :
// localStorage.setItem("userName","Alex")

// // data received :
// let Namee = localStorage.getItem("userName")
// console.log(Namee);

// // remove data:
// localStorage.removeItem("userName")
// // localStorage.clear();

//// session storage
// sessionStorage.setItem("userName","Alex")
// let Namee = sessionStorage.getItem("userName")
// console.log(Namee);

////// Immediately Invoked Function Expression (IIFE)

// (function () {
//     console.log("hi hello");
    
// })()

////// reduce method 
const number = [10,20,30,40]

const total = number.reduce((acc, current)=>{
    return acc + current
},20)

console.log(total);//120

const max = number.reduce((acc,current)=>{
    return current > acc ? current : acc;
},number[0])

console.log(max);//40 

const cart = [
    { product: 'Shirt', price : 500 },
    { product: 'Pant', price : 400 },
    { product: 'Shoe', price : 300 }
]

const totalPrice = cart.reduce((acc,item)=>{
    return acc + item.price 
},0)

console.log(totalPrice); 

////// Map 
const numbers = [1,2,3,4,5]
const double = numbers.map((num, index)=>{
    return num*2
})
console.log(numbers); 
console.log(double); 

////// optional chaining

const user = {
    name : "skd",
}
console.log(user?.address?.city);//undefined 
console.log(user?.name);//skd 

////// Nullish Coalescing (??)
let data = null;
let res = data ?? "default"
console.log(res);
