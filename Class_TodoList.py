class TodoList:
    def __init__(self):
        self.tasks = []

    def __setitem__(self, key, value):
        self.tasks.append(value)

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)