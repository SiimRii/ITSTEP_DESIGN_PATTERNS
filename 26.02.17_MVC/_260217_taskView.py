

class TaskView:
    def __init__(self):
        pass


    # adding | deleting tasks:
    def added_task(self, task):
        print(f"Task '{task.name}' added to the list.")

    def deleted_task(self, task_name):
        print(f"Task '{task_name}' deleted from the list.")


    # displaying tasks:
    def display_tasks(self, tasks):
        print("Tasks:")
        for task in tasks:
            status = "Yes" if task.complete else "No"
            print(f" - {task.name} - completed: {status}")

    def display_finished_tasks(self, tasks):
        print("Finished tasks are:")
        for task in tasks:
            print(f" - {task.name}")
        print(f"Number of all finished tasks: {len(tasks)}")

    def none_finished_tasks(self):
        print("No finished tasks found.")


    # finishing tasks:
    def task_not_found(self, task_name):
        print(f"Task '{task_name}' was not found.")

    def finished_task(self, task_name):
        print(f"Task '{task_name}' was completed.")


        