import argparse
import json
from project import Project
from task import Task

def load_project():
    try:
        with open('project_data.json', 'r') as file:
            project_data = json.load(file)
            project = Project()
            project.next_key = project_data['next_key']
            
            for task_data in project_data['tasks']:
                project.tasks[task_data['key']] = Task(task_data['key'], task_data['name'], task_data['duration'])
                
            for dep_data in project_data['dependencies']:
                project.add_dependencies(dep_data['task'], dep_data['dependencies'])
                
            return project
    except FileNotFoundError:
        return Project()

def save_project(project):
    project_data = {
        'next_key': project.next_key,
        'tasks': [{'key': task.key, 'name': task.name, 'duration': task.duration} for task in project.tasks.values()],
        'dependencies': [{'task': task.key, 'dependencies': [dep.key for dep in task.dependencies]} for task in project.tasks.values()]
    }
    with open('project_data.json', 'w') as file:
        json.dump(project_data, file, indent=4)

def add_task(name, duration, dependencies):
    project = load_project()
    task_key = project.add_task(name, duration)
    
    if dependencies:
        dependency_keys = list(map(int, dependencies.split(',')))
        project.add_dependencies(task_key, dependency_keys)
        
    save_project(project)
    print(f"Task '{name}' with duration {duration} added successfully with key {task_key}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a task to the project")
    parser.add_argument('--name', required=True, help="Name of the task")
    parser.add_argument('--time', type=int, required=True, help="time for the task in days")
    parser.add_argument('--dep', help="Comma-separated list of dependency keys", default="") #Shortened Dependencies to Dep, no word should have to be 11 letters
    args = parser.parse_args()
    
    add_task(args.name, args.time, args.dep)
