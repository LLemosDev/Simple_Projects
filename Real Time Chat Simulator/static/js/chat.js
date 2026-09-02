const socket = io() // represent the connection with server

// testing connection

socket.on("message", function(data){
    console.log(data)
})

// testing connection 
socket.emit("test_connection", {
    message: "test connection client-server"
})

const send_button = document.getElementById("send-btn")
const message_section = document.querySelector(".messages")
const input = document.getElementById('input')


// Event listener execute the follow function every time user click on send-btn
send_button.addEventListener('click', (event) =>{
    event.preventDefault()

    let message = input.value

    // Send event 
    socket.emit("send_message", {
        message: message
    })

    // Clear input
    input.value = ""
    
})

// Wait until the server process the message sent and then call the function below:
socket.on("receive_message", function(data){

    // Creating elemeents
    const message = document.createElement('div')
    const message_avatar = document.createElement('div')
    const message_content = document.createElement('div')

    // Assign class
    message.classList.add("message")
    message_avatar.classList.add("message-avatar", `${data.user_color}`)
    message_content.classList.add('message-content')

    // Show the data received
    message_avatar.textContent = data.username[0].toUpperCase()
    message_content.innerHTML = `<strong>${data.username}</strong><p>${data.message}</p>`

    // Appending into parent node
    message.appendChild(message_avatar)
    message.appendChild(message_content)

    // Appending into mainly node
    message_section.appendChild(message)
})