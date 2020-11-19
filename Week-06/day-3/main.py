import sys
import pickle

try:
    TasksFile = open('tasks.txt', 'rb')
    # LoadedTasks contains the tasks and their Done status as a boolean
    # it's structured like : [['Task Description',True],['Task2 Description',False]]
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
        LoadedTasks.append([TaskDescription,False])
        pickle.dump(LoadedTasks, open('tasks.txt', 'wb'))
    except IndexError:
        print("Unable to add: no task provided")
elif "-l" in sys.argv:
    # If the LoadedTasks variable is empty provide the
    # correct error message
    if not LoadedTasks: #If it's empty
        print("No todos for today! :)")
    else :
        for task in LoadedTasks:
            LoadedTaskIndex = str(LoadedTasks.index(task)+ 1)
            if task[1]: # If the task is done
                print(LoadedTaskIndex + " - [X] " + task[0])
            else: # the task has not been completed yet
                print(LoadedTaskIndex + " - [ ] " + task[0])
elif "-r" in sys.argv:
    try:
        TaskNumber = sys.argv[2] # Task number to be removed
    except IndexError: # Add error catching
        print("Unable to remove: no index provided")
        exit()
    try:
        LoadedTasks.pop(int(TaskNumber) - 1)  # Remove the task from the LoadedTasks list
        pickle.dump(LoadedTasks, open('tasks.txt', 'wb'))  # Write again to file
    except IndexError:
        print("Unable to remove: index is out of bound")
    except ValueError:
        print("Unable to remove: index is not a number")
elif "-c" in sys.argv:
    try:
        TaskNumber = sys.argv[2]  # Task number to be checked
    except IndexError: # Add error catching
        print("Unable to remove: no index provided")
        exit()
    try:
        TaskNumber = int(TaskNumber) - 1
        LoadedTasks[TaskNumber][1] = True
        pickle.dump(LoadedTasks, open('tasks.txt', 'wb'))
    except IndexError:
        print("Unable to remove: index is out of bound")
    except ValueError:
        print("Unable to remove: index is not a number")
else: #If none of the above conditions matched than the wrong argument must be provided
    print("Unsupported argument")