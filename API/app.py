# Lets create a flask web application
from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Learning API in depth'


tasks = [
    {
        'id': 1,
        'title':'100 days of code',
        'description': 'Python',
        'done': False,
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_task():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
