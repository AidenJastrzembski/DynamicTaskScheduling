import json
import argparse
from scripts.project import Project, create_sample_project
from scripts.scheduler import schedule_tasks
from scripts.task import Task

def load_project():
    try:
        with open('scripts/project_data.json', 'r') as file:
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

def main():
    parser = argparse.ArgumentParser(description="Run the task scheduler")
    parser.add_argument('--sample', action='store_true', help="Use the sample project")
    args = parser.parse_args()
 
    if args.sample:
        project = create_sample_project()
    else:
        project = load_project()
    
    start_times, finish_times = schedule_tasks(project)

    for task in project.tasks.values():
        print(f"Task {task.key} ({task.name}): Start Time = {start_times[task]}, Finish Time = {finish_times[task]}")

if __name__ == "__main__":
    main()
