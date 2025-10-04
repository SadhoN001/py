// document.writeln("<br> yaahaa habibi")

// // console.log("hi friend")

// // const fruits= ['mango', 'banana', 'apple']
// // console.log(typeof(fruits))

// // let i=1;
// // do{
// //     console.log(i);
// //     i++;
// // }while(i<=5);

// // for(let i in fruits){
// //     console.log(i)
// // }

// /* Array method */

// const num =[1,2,3,4,5,6]
// console.log(num.at(2))

// const a=['a','b','c']
// const b=['x','y','z']
// console.log(a.concat(b))//['a', 'b', 'c', 'x', 'y', 'z']

// console.log(num.every((n)=>n%2===0)) // false
// console.log(num.filter((n)=>n>0)) // [1,2,3,4,5,6]
// console.log(num.find((n)=> n>2))// 3
// console.log(num.findIndex((n)=>n===3))//2

// const str="hello"
// console.log(Array.from(str))// ['h', 'e', 'l', 'l', 'o']

// console.log(num.includes(3))// true
// console.log(a.join(" "))//a b c (string)

// const n= [1,2,3,2,2,4,2]
// console.log(n.lastIndexOf(2))// 6
// console.log(n.length)// 7
// console.log(n.pop())//2
// n.push(11)
// console.log(n)// [1, 2, 3, 2, 2, 4, 11]
// console.log(n.shift())
// console.log(n)// [2, 3, 2, 2, 4, 11]
// n.reverse()
// console.log(n)// [11, 4, 2, 2, 3, 2]

// const numsort = [1,3,2,5,3,4,6]
// console.log(numsort.sort())// [1, 2, 3, 3, 4, 5, 6]
// console.log(n.sort((a,b)=>a-b))//  [2, 2, 2, 3, 4, 11] assending
// console.log(n.sort((a,b)=>b-a))//  [11, 4, 3, 2, 2, 2] desenfing
// console.log(n.slice(1,3))// [4, 3]
// console.log(n.some((n)=>n%2===0))// true (1 ta sorto puron korlei)
// n.splice(0,0,100)
// console.log(n)// [100, 11, 4, 3, 2, 2, 2]
// console.log(n.toLocaleString())// 100,11,4,3,2,2,2
// n.unshift(777)
// console.log(n)//  [777, 100, 11, 4, 3, 2, 2, 2]


// /* String method */

// /*  Date Object*/
// const noww = new Date("2001-05-13")
// console.log(noww)

// const now = new Date();
// console.log(now)
// console.log(now.getFullYear())// 2025
// console.log(now.getMonth())// 8
// console.log(now.getDate())// 27 
// console.log(now.getHours())// 20
// console.log(now.getMinutes())// 36
// console.log(now.getSeconds())
// console.log(now.getTime())

// const date = new Date();
// date.setFullYear(2025)
// date.setMonth(8)
// date.setDate(27)
// console.log(date)

// const start = new Date("2001-05-13")
// const end = new Date("2025-09-27")
// const diff = end -start
// const days = diff/(1000*60*60*24)
// console.log(diff)
// console.log(days)// 8903 days

// let bdTime = date.toLocaleString("en-BD")
// console.log(bdTime)


// /* math */
// console.log(Math.round(4.6))// 5
// console.log(Math.round(4.4))// 4
// console.log(Math.floor(4.9))// 4
// console.log(Math.ceil(4.1))// 5
// console.log(Math.PI)// 3.141592653589793
// console.log(Math.sqrt(4))// 2
// console.log(Math.pow(2,3))// 8
// console.log(Math.abs(-8))// 8
// console.log(Math.min(6,4,3,5,2,9))// 2
// console.log(Math.max(6,4,3,5,2,9))// 9
// console.log(Math.random())
// console.log(Math.floor(Math.random()*100)+1)// 100 er nich porjonto count

/* Number */
// let num = 1234546;
// console.log(num.toExponential())// 1.234546e+6
// let num = 3.1456;
// console.log(num.toFixed(2))// 3.15
// let num = 1234567.89;
// console.log(num.toLocaleString("en-US"))// 1,234,567.89
// console.log(num.toLocaleString("bn-BD"))// 1,234,567.89

// let num = 1234546;
// console.log(num.toPrecision(4))// 1.234546e+6
// console.log(num.toString())// 1234546
// console.log(num.valueOf())// 1234546

// let str = "12345.46";
// console.log(parseInt(str))// 12345
// console.log(parseFloat(str))// 12345.46
// console.log(String(str))// 12345.46

// console.log(Number.MAX_VALUE)
// console.log(Number.MIN_VALUE)


// let nan = 344/"hi"
// console.log(nan)//NaN

