class TodoList:
    def __init__(self):
        self.tasks = []
        self.step = 1


    def __setitem__(self, key, value):
        self.tasks.append(value)

    def __getitem__(self, item):
        return self.tasks[item]

    def __iter__(self):
        self.start = -1
        return self

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)

    def __next__(self):
        if self.start < len(self.tasks) - 1:
            self.start += self.step
            return self.tasks[self.start]
        else:
            raise StopIteration