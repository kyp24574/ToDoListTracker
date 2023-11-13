# ToDoListTracker
Simple python program for a to-do list!

This To-Do List Tracker contains only 4 commands:
Show, Add, Remove, and Exit.

The Show command displays the tasks located in the to-do list file
in a numbered format via the terminal. If no list exists, or the list
is empty, the method displays the phrase 'Nothing in the list!'

The Add command appends a task at the end of the to-do list file.
This command also creates a to-do list file if one does not exist.

The Remove command deletes a task from the to-do list file.
If the task is located at the end of the list, it is removed.
If it is located at the beginning or middle of the list, the entire file is
re-written without that specific task, essentially "removing" that task
from the list.

The Exit command simply exits the program.
