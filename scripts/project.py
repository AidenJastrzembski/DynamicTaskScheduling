from scripts.task import Task

class Project:
    def __init__(self):
        self.tasks = {}
        self.next_key = 1

    def add_task(self, name, time):
        key = self.next_key
        self.next_key += 1
        self.tasks[key] = Task(key, name, time)
        return key

    def add_dependencies(self, task_key, dependency_keys):
        if task_key in self.tasks:
            for dep_key in dependency_keys:
                if dep_key in self.tasks:
                    self.tasks[task_key].add_dependency(self.tasks[dep_key])

def create_sample_project():
    project = Project()
    a = project.add_task('Gather Wake Word / Non Wake Word Data', 5)
    b = project.add_task('Create script to omit certain aspects from wakeword data', 3)
    c = project.add_task('Prepare training data', 2)
    d = project.add_task('Train model', 4)
    e = project.add_task('Evaluate model', 1)
    
    project.add_dependencies(b, [a])
    project.add_dependencies(c, [a, b])
    project.add_dependencies(d, [c])
    project.add_dependencies(e, [d])

    return project
