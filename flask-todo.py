from flask import Flask, render_template, request

from models.todos import TodoModel
import json
app = Flask(__name__)

DATABASE = 'db.db'


@app.route('/', methods=['GET'])
def hello_world():

    todos = []
    with TodoModel() as Todo:
        todos_data = Todo.get_todos_all()
        for todo in todos_data:
           todos.append({
               'id' : todo.id,
               'task': todo.todo,
               'done': todo.done
           })

    return render_template(
        'top.html',
        todos=todos
    )


@app.route('/todo', methods=['POST'])
def add_todo():
    print(request.json)
    with TodoModel() as Todo:
        todo = Todo.register_todo(request.json['task'])
        data = {'id': todo.id, 'task': todo.todo, 'done': False}

    print(data)
    return json.dumps(data)

@app.route('/todo', methods=['DELETE'])
def del_todo():
    with TodoModel() as Todo:
        Todo.del_todo(int(request.json['id']))

    return ''

if __name__ == '__main__':
    app.run()
