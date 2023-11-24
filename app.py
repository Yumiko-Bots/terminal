from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_code')
def execute_code(data):
    try:
        # Execute the Python code
        result = str(eval(data['code']))
    except Exception as e:
        result = str(e)
    # Send the result back to the client
    socketio.emit('execution_result', {'result': result})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
