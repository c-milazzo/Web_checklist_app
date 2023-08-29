import streamlit as st
import Functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)

todos = Functions.get_todos()

st.title('My Checklist')
st.subheader('This is my checklist')
st.write('This app is to increase your productivity'
         ' by allowing you to keep track of tasks that need '
         'to be completed.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a task that needs completion: ', placeholder="Enter a task: ",
              on_change=add_todo, key='new_todo')