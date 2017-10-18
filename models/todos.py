from models.models import *

class TodoModel():

    def __init__(self):
        self.closed = False
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def close(self):
        if self.closed:
            return
        self.session.closed = True
        self.session.close()

    def get_todos_all(self):
        '''
        ユーザ全員の情報をリストで返す
        :return: [User1, User2, ...]
        '''
        todos_data = self.session.query(Todo).all()
        self.session.flush()
        data = []
        return todos_data

    def get_todo_by_id(self, id=-1):
        '''
        idで指定したユーザ１人を返す
        :param id: int
        :return: User
        '''
        todo_data = self.session.query(Todo).filter_by(id=id).first()
        return [todo_data]

    def register_todo(self, task):
        '''
        新しいユーザを登録
        :param name: string
        :return: User
        '''
        new_todo = Todo(todo=task, done=False)
        self.session.add(new_todo)
        self.session.flush()
        self.session.commit()
        return {'task': new_todo.todo, 'done': False}