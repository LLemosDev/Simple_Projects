from flask import Flask, session, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room
import secrets

# Create Flask app instance 
app = Flask("__name__")

# Sercet key is necessary to use session
app.secret_key = secrets.token_hex(32)

# Create SocketIO instance
socket = SocketIO(app)

# Basic home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username

        return redirect(url_for('chat'))

    else:
        return render_template("index.html")


# Get username and redirect for chat page
@app.route("/chat")
def chat():
    if "username" not in session:
        return redirect(url_for('index'))
    else:
        return render_template("chat.html")


# Socket events
# .on(): listen to an event, wait until client send an event
# .emit(): send an event

# Conection and desconection are reserved events and already have a function
@socket.on("connect")
def handle_connection():
    # Send message to test connection
    socket.emit("message", {
        "text": "Connection established!"
    })

    # Join General room as standart
    join_room("general")
    session["room"] = "general"
    print("User joined General")

@socket.on("test_connection")
def handle_test_connection(data):
    print(data)

# obs: it's possible to use any name for param event,
# the important thing is: the server and client must be using the same event name

@socket.on("send_message")
def handle_send_message(data):
    username = session["username"]
    # Send an event
    socket.emit("receive_message", {
        "username": username,
        "message": data["message"]
    },
    to=session["room"])    # Send the message to all the users in the given room


if __name__ == '__main__':
    socket.run(app, debug=True)

