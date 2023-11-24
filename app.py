from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_code')
def execute_code(data):
    try:
        result = str(eval(data['code']))
    except Exception as e:
        result = str(e)
    socketio.emit('execution_result', {'result': result})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080)
