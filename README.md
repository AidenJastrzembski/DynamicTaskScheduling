# Dynamic Task Scheduling

This implements a dynamic task scheduling algorithm for managing tasks with dependencies and varying durations. The algorithm determines the optimal order of task execution to minimize the total project time span.

Requirements
Python 3.x

Downloading:

Clone the repository:
git clone https://github.com/AidenJastrzembski/DynamicTaskScheduling.git

If you don't have Git installed, you can download the repository as a ZIP file and extract it.

## Add Tasks with add_task.py

cd to scripts/

python add_tasks.py --name "Name" --duration (int) --dependancies "1,2"

--dependancies is optional (intakes a list of keys)

Running this will automatically create the json file and add your task to it.

## Run with tasks from the JSON file

python main.py

## Run with the sample project

python main.py --sample
--sample option runs the scheduler with the predefined sample project.
