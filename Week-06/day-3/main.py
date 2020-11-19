import sys
import pickle

try:
    TasksFile = open('tasks.txt', 'rb')
    LoadedTasks = pickle.load(TasksFile)
except EOFError:
    LoadedTasks = {}

if len(sys.argv) == 1 :
    print("""Command Line Todo application
    =============================

    Command-line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes a task
        -c   Completes a task
    """)
elif "-a" in sys.argv:
    print("You asked to add a task")
elif "-l" in sys.argv:
    # If the LoadedTasks variable is empty provide the
    # correct error message
    if not LoadedTasks:
        print("No todos for today! :)")

#pickle.dump(tasksObject,TasksFile)
