
from _260217_task import Task


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    

    def add_task(self, task_name):
        task = Task(task_name)
        self.model.add_task(task)
        self.view.added_task(task)


    def delete_task(self, task_name):
        if self.model.delete_task(task_name):
            self.view.deleted_task(task_name)
        elif self.model.delete_task(task_name) == False:
            self.view.task_not_found(task_name)
        

    def finish_task(self, task_name):
        task = self.model.get_task(task_name)

        if task is None:
            self.view.task_not_found(task_name)
        else:
            task.complete = True
            self.view.finished_task(task_name)


    # displaying:
    def show_finished_tasks(self):
        tasks = self.model.get_finished_tasks()

        if tasks is None:
            self.view.none_finished_tasks()
        else:
            self.view.display_finished_tasks(tasks)


    def show_tasks(self):
        all_tasks = self.model.get_tasks()
        self.view.display_tasks(all_tasks)



