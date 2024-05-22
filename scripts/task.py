class Task:
    def __init__(self, key, name, duration):
        self.key = key
        self.name = name
        self.duration = duration
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)
