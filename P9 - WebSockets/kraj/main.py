from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'tajna...'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print('SPOJEN', request.sid)

@socketio.on('disconnect')
def disconnect():
    print('ODSPOJEN', request.sid)

# custom named event (chat_message)
@socketio.on('chat_message') 
def chat_message(message):
    print('message: ', message)
    emit('chat_message', message, broadcast=True)



