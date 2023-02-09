import streamlit as sl
import functions

todos = functions.read_file()


def add_todo():
    todo = sl.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_file(todos)


sl.title("My Todo App")
sl.write("This App has been made with Streamlit library of Python.")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.text_input(label="", placeholder="Enter your tasks...", key="new_todo", on_change=add_todo)

print("<<< END >>>")
