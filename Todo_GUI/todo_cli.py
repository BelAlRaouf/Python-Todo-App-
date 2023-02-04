import functions

while True:

    user_action = input("Write down add, edit, remove show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.read_file()

        todos.append(todo + '\n')

        functions.write_file(todos)

    elif user_action.startswith('show'):
        todos = functions.read_file()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            items = f"{index + 1} - {item}"
            print(items)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.read_file()

            new_todo = input("enter your new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_file(todos)
        except ValueError:
            print('please enter the index number!')
            continue

    elif user_action.startswith('remove'):
        try:
            deleted_item_index_number = int(user_action[6:])

            todos = functions.read_file()

            removed_item = todos.pop(deleted_item_index_number - 1)

            functions.write_file(todos)

            print("The ", removed_item.strip('\n'), "removed from the list successfully!")

        except IndexError:
            print("please enter a number between 1 and ", len(todos), " ")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("wrong input try again!")

print("<<< \END >>>")


