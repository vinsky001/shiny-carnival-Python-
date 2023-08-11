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

# Lets update in our database using PUT method
app.route('/todo/api/v1.0/task', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(404)
    if 'descrption' in request.json and type(request.json['description']) is not unicode:
        abort(404)
    if 'done'in request.json and type(request.json['done']) is not bool:
        abort(404)
    task[0]['task'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done']) 
    return jsonify({'task': task[0]})

#Lets detete data in task using DELETE method
@app.route('/todo/api/v1.0/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    task.remove(task[0])
    return jsonify({'result': True})       
                                            
if __name__ == '__main__':
    app.run(debug=True)
