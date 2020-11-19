import sys
import pickle

try:
    TasksFile = open('tasks.txt', 'rb')
    LoadedTasks = pickle.load(TasksFile)
except EOFError:
    LoadedTasks = []

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
    # Check if the task description is provided after the -a parameter
    # before adding it to the list and saving to file
    try:
        TaskDescription = sys.argv[2]
        LoadedTasks.append(TaskDescription)
        pickle.dump(LoadedTasks, open('tasks.txt', 'wb'))
    except IndexError:
        print("Unable to add: no task provided")
elif "-l" in sys.argv:
    # If the LoadedTasks variable is empty provide the
    # correct error message
    if not LoadedTasks: #If it's empty
        print("No todos for today! :)")
    else :
        print(LoadedTasks)