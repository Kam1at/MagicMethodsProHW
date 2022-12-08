import datetime
from Class_TodoList import TodoList

class Task:

    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().replace(microsecond=0)

    def __keys(self):
        return f"{self.content} (создано {str(self.date)})"

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__keys() == other.__keys()
        return NotImplemented

    def __hash__(self):
        return hash(self.__keys())

    def __repr__(self):
        return f"{self.__keys()}"

    def __len__(self):
        return len(self.content)

    def __bool__(self):
        return bool(len(self.content))






todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('кофе')
todo_list[2] = Task('Выпить')
todo_list[3] = Task('Выпить кофе')
todo_list[4] = Task('Выпе')
todo_list[5] = Task('итьфе')
# print(todo_list)

for item in todo_list:
    print(item)
