// // // some data take time sending and receving
// // // console.log("1")
// // // console.log("3")
// // // setTimeout(() =>console.log("2  "),2000);

// // // promise :promise is a type o promise know data is not coming but in future 
// // // they are three types 
// // // 1)pending
// // // 2)fulfilled
// // // 3)rejected
// // // pending and rejected----------
// // let promise = new Promise((resolve,reject)=>{
// //     let success =true;
// //     if (success){
// //         resolve("IT worked");
// //     }
// //     else{
// //         reject("something went wrong here");
// //     }
   
// // });
// // function whenResolve(data){
// //     console.log(data);
// // }
// // function whenReject(data){
// //     console.log(data);
// // }
// // promise.catch(whenReject) //catch mean when data is reject

// // promise.then(whenResolve)// then mean when data is successfuly


// // // when we add settime method in promise
// // ===========================promise====================
// // promise: it is like a promise  so some data not  coming but probality he is coming in future 
// // they are three types:-
// // 1) fullfilled(.then)
// // 2)rejected(.catch)
// // 3)pending 
// // let promise = new Promise((resolve ,reject)=>{
// //     let success = true;
// //     if (success){  
// //         resolve("it work.....");

// //     }
// //     else{
//     //         reject("it's not working.....");
//     //     }
    
//     // });
    
// // function whenresolve(data){
// //         console.log(data);    
// // }
// // function whenreject(data){
// //     console.log(data);
// // }

// // promise.then(whenresolve);
// // promise.catch(whenreject);
// // setTimeout:---
// //  console.log("teenu takeya bina ni dil rajdaaa.......");
// // let b = setTimeout(() =>console.log("muhalle vichon kooch na kari......"),1500);
// // setTimeout(()=> console.log("deva vasta hoo biba sone rab da maholle vichon kooch na kari....."),5000);
     











// // ===========================================promises===================================
// // const add =(a,b) => a+b;
// // arrow function
// // what is promise  :a promose  is an object represnting  a value that isn't available 
// //they have 2 condition resolved and reject
// let promise = new Promise((resolve ,reject) => {
// let a ="systems online"
// let b = setTimeout(() =>console.log(a),3000);
//     let success = true;
//     if (success ){
//         resolve("");
//     }
//     else {
//         reject ("some libres not download")
//     }
// })
    
// function fetchData(){
//     let promise = new Promise((resolve,reject)=>{
//         msg = "something"

//         setTimeout(()=>{
//             resolve("msg received")
//         },3000); 
//     })
//     return promise
// }
// async function run(){
//     let data = await fetchData()
//     console.log(1)
//     console.log(2)
// }
// run()

// console.log("loading...   ")




