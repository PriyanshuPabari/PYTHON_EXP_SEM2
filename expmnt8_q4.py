import tkinter as tk
from tkinter import simpledialog
import sqlite3
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
conn.commit()
def load_tasks():
    listbox.delete(0, tk.END)
    for row in cursor.execute("SELECT task FROM tasks"):
        listbox.insert(tk.END, row[0])
def add_task():
    task = simpledialog.askstring("Add Task", "Enter task:")
    if task:
        cursor.execute("INSERT INTO tasks VALUES (?)", (task,))
        conn.commit()
        load_tasks()
def delete_task():
    selected = listbox.get(tk.ACTIVE)
    cursor.execute("DELETE FROM tasks WHERE task=?", (selected,))
    conn.commit()
    load_tasks()

def update_task():
    selected = listbox.get(tk.ACTIVE)
    new_task = simpledialog.askstring("Edit Task", "Update task:", initialvalue=selected)
    if new_task:
        cursor.execute("UPDATE tasks SET task=? WHERE task=?", (new_task, selected))
        conn.commit()
        load_tasks()
root = tk.Tk()
root.title("Task Manager")
listbox = tk.Listbox(root, width=40)
listbox.pack()
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Edit Task", command=update_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()
load_tasks()
root.mainloop()