# Lets create a flask web application
from flask import Flask , jsonify, abort, make_response, request

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

"""
Here we get the id of the task in the URL, 
and Flask translates it into the task_id argument that we receive in the function.
With this argument we search our tasks array. 
If the id that we were given does not exist in our database then we return the familiar error code 404, 
which according to the HTTP specification means "Resource Not Found", which is exactly our case.
 """
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_specific_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Lets insert an item in our database using POST method
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['My python sprint'],
        'description': request.json.get('Description', 'In progress'),
        'done': False
        
    }    
    tasks.append(task) 
    return jsonify({'tasks': task }), 201   

app.route('/') 

if __name__ == '__main__':
    app.run(debug=True)
