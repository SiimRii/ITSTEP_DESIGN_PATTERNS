

class TaskModel:
    def __init__(self):
        self.tasks = []
        self.finished_tasks = []

    
    # adding | deleting | getting task/-s:
    def add_task(self, task):
        self.tasks.append(task)


    def delete_task(self, task_name):
        task_to_be_deleted = self.get_task(task_name)
        if task_to_be_deleted is not None:
            self.tasks.remove(task_to_be_deleted)
            return True
        else:
            return False


    def get_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None
    """
    def get_task(self, task_name):
        return next((task for task in self.tasks if task.name == task_name), None)
    """


    def get_tasks(self):
        return self.tasks


    def get_finished_tasks(self):
        for task in self.tasks:
            if task.complete:
                self.finished_tasks.append(task)
        
        return self.finished_tasks


    
    
