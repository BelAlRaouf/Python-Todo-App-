import functions
import PySimpleGUI as sg

label = sg.Text("Type To-Do's Here: ")
input_box = sg.InputText(tooltip="Enter todos ", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.read_file(), key="todos",
                      enable_events=True, size=(44, 10))
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Arial", 20))

while True:

    event, values = window.read()
    print(1, event)
    print(2, values)
    print(2, values['todos'])
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.read_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_file(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            todo_to_complete = values['todos'][0]

            todos = functions.read_file()
            index = todos.index(todo_to_complete)
            removed_item = todos.pop(index)
            functions.write_file(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
