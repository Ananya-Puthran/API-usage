let currentTheme = "default"

function setTheme(theme){
currentTheme = theme
}

function sendMessage(){

const input = document.getElementById("userInput")
const text = input.value

if(text === "") return

addMessage(text,"user")

setTimeout(()=>{
addMessage("AI responding in " + currentTheme + " style","ai")
},500)

input.value=""
}

function addMessage(text,type){

const container = document.getElementById("messages")

const message = document.createElement("div")

message.classList.add("message",type)

message.innerText = text

container.appendChild(message)

container.scrollTop = container.scrollHeight
}

function toggleSidebar(){

document.getElementById("sidebar").classList.toggle("collapsed")

}