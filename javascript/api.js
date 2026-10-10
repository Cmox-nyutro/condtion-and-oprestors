// api (application programming interface) is transfer request frontend to backend   .basically commnicate btwn two application 
// fetch api: fetch is bult in function makking http request
// async function ge(){
//     const response = await fetch("https://jsonplaceholder.typicode.com/users")
//     const data = await response.json()
//     console.log(data)

// }
// ge()

function rand(){
    const le = new Promise((resolved,reject) =>{
        let success = true
        if (success === true){
            resolved("this is the date")
        }else{
            reject("value is reject")
        }
    })

}
async function ge(){
    try{
        const ans = await rand()
    }catch(error){
console.log(error)
    }
    
}
ge()
          