const rooms = document.querySelectorAll(".room")
const chat_name = document.getElementById('chat-name')
var current_btn = document.querySelector('.active')

rooms.forEach(btn => {
    btn.addEventListener('click', () =>{

        let room = btn.value

        // Removing .active class to the old btn
        current_btn.classList.remove('active')

        // Setting current btn and .active class
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