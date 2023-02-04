def read_file():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    return todos


def write_file(todos_arg):
    with open('todo.txt', 'w') as file:
        file.writelines(todos_arg)

