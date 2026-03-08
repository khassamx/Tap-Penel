let taps = 0
let active = 0

function tap(){

taps += 3

document.getElementById("tapCount").innerText = taps

}

function login(){

let gmail = document.getElementById("gmail").value
let pass = document.getElementById("password").value

if(gmail && pass){

active += 1
document.getElementById("active").innerText = active

}else{

alert("Completa los datos")

}

}