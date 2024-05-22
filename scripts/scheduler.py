from collections import deque

def topological_sort(project):
    in_degree = {task: 0 for task in project.tasks.values()} #Dictionary to store number of incoming edges of each task
    
    for task in project.tasks.values(): #Build the edges out
        for dependency in task.dependencies:
            in_degree[task] += 1
    
    queue = deque()

    for task, degree in in_degree.items():
        if degree == 0:
            queue.append(task) #for all degree 0, add to queue
        
    sorted_tasks = []

    while queue:
        task = queue.popleft()
        sorted_tasks.append(task)
        
        for dependent in project.tasks.values():
            if task in dependent.dependencies:
                in_degree[dependent] -= 1
                
                if in_degree[dependent] == 0:
                    queue.append(dependent)
    
    return sorted_tasks

def schedule_tasks(project):
    sorted_tasks = topological_sort(project)
    start_times = {}
    for task in project.tasks.values():
        start_times[task] = 0 #Init start times to be 0
        
    finish_times = {}

    for task in sorted_tasks:
        start_time = max((finish_times[dependency] for dependency in task.dependencies), default=0)
        finish_time = start_time + task.duration
        start_times[task] = start_time
        finish_times[task] = finish_time

    return start_times, finish_times
