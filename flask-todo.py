from flask import Flask, render_template, request

from models.todos import TodoModel
import json
app = Flask(__name__)

DATABASE = 'db.db'


@app.route('/', methods=['GET'])
def hello_world():

    with TodoModel() as Todo:
        todos = Todo.get_todos_all()

    return render_template(
        'top.html',
        todos=todos)


@app.route('/todo', methods=['POST'])
def add_todo():
    print(request.json)
    with TodoModel() as Todo:
        todo = Todo.register_todo(request.json['task'])
        data = {'task': todo['task'], 'done': False}

    return json.dumps(data)

if __name__ == '__main__':
    app.run()
