"""Laboratorio 8 - CLI del gestor de tareas."""
"""Laboratorio 8 - CLI del gestor de tareas."""
 

import sys
from todo_manager import read_todo_file, write_todo_file
 
def main():
    
    if len(sys.argv) < 2:
        print("Insufficient arguments provided!")
        return
 
    # HELP
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
 
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
""")
        return
 
    file_path = sys.argv[1]
    tasks = read_todo_file(file_path)

    write_todo_file(file_path, tasks)
 
    i = 2
    modified = False
 
    while i < len(sys.argv):
        command = sys.argv[i]
 
        if command == "add":
            if i + 1 >= len(sys.argv):
                print('Task description required for "add".')
                return
 
            task = sys.argv[i + 1]
            tasks.append(task)
            print(f'Task "{task}" added.')
            modified = True
            i += 2
 
        elif command == "remove":
            if i + 1 >= len(sys.argv):
                print('Task description required for "remove".')
                return
 
            task = sys.argv[i + 1]
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
                modified = True
            else:
                print(f'Task "{task}" not found.')
            i += 2
 
        elif command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
            i += 1
 
        else:
            print("Command not found!")
            return
 
    if modified:
        write_todo_file(file_path, tasks)
 
 
if __name__ == "__main__":
    main()
 