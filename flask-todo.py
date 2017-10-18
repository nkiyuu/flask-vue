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
        data = {'task': todo['task'], 'done': False}

    return json.dumps(data)

if __name__ == '__main__':
    app.run()
