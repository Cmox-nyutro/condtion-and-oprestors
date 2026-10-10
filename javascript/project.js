const input = document.getElementById("int");;
const btn = document.getElementById("btn");
const diw = document.getElementById("di")

function addTask(){
    if(input.value === '')
        alert("you must be write something here......");
    else{
        let li = document.createElement("li");
        li.innerHTML =input.value; //?
        diw.appendChild(li);
        input.value =" "; //after write text text is still there
        let com = document.createElement("span");
        span.innerHTML = "\u0087";
        li.appendChild(span); //?
        const delbtn =document.getElementById("btn")
        delbtn.textContent ="Delete"
        li.appendChild(delbtn)
        delbtn.addEventListener("clcik",() =>del(btn.id))
    }

}