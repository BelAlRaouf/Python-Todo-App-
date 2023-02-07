import functions
import PySimpleGUI as sg

label = sg.Text("Type To-Do's Here: ")
input_box = sg.InputText(tooltip="Enter todos ", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Arial", 20))

while True:

    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)

        case sg.WIN_CLOSED:
            break

window.close()
