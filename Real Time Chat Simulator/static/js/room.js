const rooms = document.querySelectorAll(".room")
const chat_name = document.getElementById('chat-name')
var current_btn = document.querySelector('.active')

rooms.forEach(btn => {
    btn.addEventListener('click', () =>{

        let room = btn.value

        // Removing .active class to the old btn
        current_btn.classList.remove('active')

        // Setting new current btn and .active class
        current_btn = btn
        current_btn.classList.add('active')

        // send event to server
        socket.emit("change_room", {
            room: room
        })

    })
})

socket.on("room_changed", function(data){
    chat_name.textContent = `# ${data.room}`
})

socket.on("system_message", function(data){

    system_msg = document.createElement('div')
    system_msg.classList.add('system-message')
    system_msg.textContent = data.message

    message_section.appendChild(system_msg)
})

// load history only for the user that have just joined room
socket.on("load_history", function(data){
    // clearing messages
    message_section.innerHTML = ""

    // history is an array of objects
    let history = data.history

    history.forEach(msg => {
        // Creating elemeents
        let message = document.createElement('div')
        let message_avatar = document.createElement('div')
        let message_content = document.createElement('div')

        // Assign class
        message.classList.add("message")
        message_avatar.classList.add("message-avatar", `${msg.user_color}`)
        message_content.classList.add('message-content')

        // Show the data received
        message_avatar.textContent = msg.username[0].toUpperCase()
        message_content.innerHTML = `<strong>${msg.username}</strong><p>${msg.message}</p>`

         // Appending into parent node
        message.appendChild(message_avatar)
        message.appendChild(message_content)

        // Appending into mainly node
        message_section.appendChild(message)
    })
})