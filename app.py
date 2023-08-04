from flask import Flask,request,jsonify,render_template

app= Flask(__name__)


tasks = [
    { 'id': 1,'title': "Task1",'description':'This is the Task 1 of the Python REST API', 'done': False},
    { 'id': 2,'title': "Task2",'description':'This is the Task 2 of the Python REST API', 'done': False},
    { 'id': 3,'title': "Tas3",'description':'This is the Task 3 of the Python REST API', 'done': False}
]

@app.route('/')
def welcome_tasks():
    return render_template('index.html')


@app.route('/tasks')
def get_tasks():
    print(tasks)
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id']==task_id),None)
    if task:
        return jsonify(task)
    return jsonify({'message':'The task_id not found'}), 404

@app.route('/tasks/create', methods = ['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'description' not in data:
        return jsonify({'message': 'Title andd description are required'}), 400
    
    new_task = {
        'id' : len(tasks) + 1,
        'title' : data['title'],
        'description':data['description'],
        'done': False
    }

    tasks.append(new_task)
    return jsonify(new_task),201

if __name__=='__main__':
    app.run(debug = True)