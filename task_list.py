tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# Print a list of uncompleted tasks

def count_incomplete_tasks(list):
    total_incomplete_tasks = []
    for task in list:
        if task ["completed"] == False:
            total_incomplete_tasks.append(task)
    return total_incomplete_tasks

print(count_incomplete_tasks(tasks))

# Print a list of completed tasks
def count_completed_tasks(list):
    total_completed_tasks = []
    for task in list:
        if task ["completed"] == True:
            total_completed_tasks.append(task)
    return total_completed_tasks
print(count_completed_tasks(tasks))

# Print a list of all task descriptions
def task_description_list(list):
    total_task_description = []
    for task in list:
            total_task_description.append(task ["description"])
    return total_task_description

print(task_description_list(tasks))

# Print a list of tasks where time_taken is at least a given time

def task_time_list(list):
    total_task_lists = []
    for task in list:
        if task ["time_taken"] > 10:
            total_task_lists.append(task)
    return total_task_lists

print(task_time_list(tasks))

# Print any task with a given description
def task_with_desc_list(list):
    task_desc_total = []
    for task in list:
        if task ["description"]:
            task_desc_total.append(task)
    return task_desc_total
print(task_time_list(tasks))

# Given a description update that task to mark it as complete.
tasks[0]["completed"] = True
print(tasks)

# Add a task to the list
tasks.append({"description": "Watch TV", "completed": False, "time_taken": 45})
print(tasks)