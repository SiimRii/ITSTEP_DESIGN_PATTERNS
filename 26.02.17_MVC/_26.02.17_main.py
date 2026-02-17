
from _260217_taskController import TaskController
from _260217_taskModel import TaskModel
from _260217_taskView import TaskView


#################### MAIN

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)


#adding tasks
controller.add_task("Task 1")
controller.add_task("Task 2")
controller.add_task("Task 3")

#finish some tasks
print("\nTasks to be done:")
controller.finish_task("Task 2")
controller.finish_task("Task 4")

#display finished tasks
print()
controller.show_finished_tasks()

#delete task and display tasks
print("\nDeleting tasks:")
controller.delete_task("Task 1")
print()
controller.show_tasks()


