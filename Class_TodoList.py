class TodoList:
    def __init__(self):
        self.tasks = []
        self.start = -1
        self.step = 1
        self.value = self.start - self.step

    def __setitem__(self, key, value):
        self.tasks.append(value)

    # def __getitem__(self, item):
    #     return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)

    def __next__(self):
        if self.start < len(self.tasks):
            self.start += self.step
            return self.tasks[self.start]
        else:
            raise StopIteration