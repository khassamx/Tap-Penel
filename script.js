function login(){

let gmail = document.getElementById("gmail").value
let pass = document.getElementById("password").value

fetch("/login",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
gmail:gmail,
password:pass
})
})
.then(res=>res.text())
.then(data=>{

if(data=="ok"){

window.location="dashboard.html"

}else{

document.getElementById("msg").innerText="Login incorrecto"

}

})

}

function openLive(){

let link = document.getElementById("live").value
window.open(link)

}

function openPost(){

let link = document.getElementById("post").value
window.open(link)

}