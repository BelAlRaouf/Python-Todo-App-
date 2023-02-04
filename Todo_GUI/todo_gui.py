import functions
import PySimpleGUI as sg

label = sg.Text("Type To-Do's Here: ")
input_box = sg.InputText(tooltip="Enter todos ")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout = [[label],[input_box, add_button]])
window.read()
window.close()
