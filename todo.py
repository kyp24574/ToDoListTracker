import os.path
import sys

# File name of .txt document
# If file does not exist in directory, a file
# with this name will be created
FILENAME = 'todo.txt'


def show_todo_list():
    """Displays the tasks present on the to-do list"""
    # Checks if the file exists
    check_file = os.path.isfile(FILENAME)

    # If file does not exist, or is empty, the method prints 'Nothing in the list!
    # and returns to the main program.
    if not check_file:
        print('Nothing in the list!')
        return
    with open(FILENAME, 'r') as file:
        tasks = file.readlines()
    if len(tasks) == 0:
        print('Nothing in the list!')
        return

    # i variable for counting and print task numbers
    i = 1
    # Prints every task on to-do list on terminal
    for task in tasks:
        task = task.strip('\n')
        print(f' * ({i}) ' + task)
        i += 1


def add_to_todo_list():
    """Adds a task to the to-do list"""
    # Checks if file exists
    check_file = os.path.isfile(FILENAME)
    # Prompt for user to enter task to be added to the list
    task = input('What task needs to be added? ') + '\n'

    # If file does not exist, creates file and writes to it
    if not check_file:
        with open(FILENAME, 'w') as file:
            file.write(task)
        return

    # If file exists, appends to the document
    with open(FILENAME, 'a') as file:
        file.write(task)


def remove_from_todo_list():
    """Removes a task from the to-do list"""
    # Ask user what task should be removed
    task_number = int(input('What item number should be removed? '))
    # Copies lines from file
    with open(FILENAME, 'r') as file:
        lines = file.readlines()

    # Re-writes file while omitting task specified by user
    # essentially "deleting" the task from the list
    with open(FILENAME, 'w') as file:
        task = 1
        for line in lines:
            if task != task_number:
                file.write(line)
            task += 1


def main():
    while True:  # Main program loop.
        while True:  # Asks for a valid response from the user
            response = input('show, add, remove, or exit? ')
            if response.lower() in ['show', 'add', 'remove', 'exit']:
                break
            print('Please choose from the options available.')

        # Executes method based on user's command
        if response.lower() == 'show':
            show_todo_list()
        elif response.lower() == 'add':
            add_to_todo_list()
        elif response.lower() == 'remove':
            remove_from_todo_list()
        elif response.lower() == 'exit':
            print('Goodbye!')
            sys.exit()


if __name__ == '__main__':
    main()
