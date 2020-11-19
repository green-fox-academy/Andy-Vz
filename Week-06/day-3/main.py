import sys
import pickle

if len(sys.argv) == 1 :
    print("""Command Line Todo application
    =============================

    Command-line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes a task
        -c   Completes a task
    """)


