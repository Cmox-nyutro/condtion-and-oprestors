//   arrow function 
const add =(a,b) => a+b;

// destructing array :it is a easy way to store data in variable
let fruits = ["apple","banana","grapps","mango","papaya"]
// =============== leanthy(old way)=============
let first  =fruits[4];
let second  =fruits[2];
console.log(first);
// ===================new way====================
// destructing
// let[a , b , c , d ] = fruits
// console.log(a,b,c,d);
// let [a , b  ,c , d, e, f] = fruits
// console.log(a,b,c,d,e,f);
//skiping value
// let [a, ,c,d,e] = fruits
// console.log(a,c,d,e);
//if item can't be exict
// let [a,b,c,d,e,f = "guvava"] = fruits
// console.log(a,b,c,d,e,f)
// =================distructing object============
//when we insert in list a object so we use {}
let stu ={name :"shivam" ,age :20,city:"kotdwar" ,course:"cse"};
// =====================old way============
// let n = stu.name;
// let k = stu.course;
// console.log(n);
// console.log(k);

// =======================in this case(distructing method)================
// let {name ,age,city,course} = stu;
// console.log(name,age,city,course);
// let {name :payal} = stu;
// console.log(payal);
// ===================parameters destructing===============
// function greet({name , age}){
    // console.log(`hi my name is ,${name} and my age${age} and i am currently persuing{course} and i am living{city} `);

// }
// greet(stu)


// ==================spread opretor(...)=====================
// let num1 = [1,2,3];
// let num2 = [4,5,6];
// let total = [...num1,...num2];
// console.log(total)
// using this(... three dot we combined multiple array in single var)
// copying an Array in another var
// let  b = [2,3,4,5];
// let copy = [...b];
// copy.push(6); //push is like a append
// console.log(copy);
//  =======================spread for object===============
// let a  = { name:"shivam" ,age :20 , branch:"CSE", sem:"5th"}
// let b = {...a ,city:"kotdwar"};
// console.log(b);
// =================using spread function with arguments================
// function add(a , b , c){
    // return a+b+c;
// }
// let total =  [3,4,9];
// // console.log(add(...total));
// function multi(a,b,c,d){
//     return a*b*c*d;

// }
// let k = [3,12,5,19];
// console.log(multi(...k))

// ===================rest========================
// const arr = [1,2,4,5]
// const newarr = [...arr,5,7] 
// console.log(newarr)

// function sum(...n){
//     console.log(n)
//     console.log(a+b+c+d+e)
// }
// sum(4,5,6,7,1)

let pe = [4,5,6,7,1]
let [a,b,...r] = pe
console.log(a,b,r)