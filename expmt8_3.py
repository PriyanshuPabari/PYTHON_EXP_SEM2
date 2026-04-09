import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()
def register():
    name = entry_name.get()
    email = entry_email.get()
    course = entry_course.get()

    if name == "" or email == "" or course == "":
        messagebox.showwarning("Error", "All fields are required")
        return

    cursor.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                   (name, email, course))
    conn.commit()
    messagebox.showinfo("Success", "Student Registered")

    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)
root = tk.Tk()
root.title("Student Registration")
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Email").grid(row=1, column=0)
tk.Label(root, text="Course").grid(row=2, column=0)
entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_course = tk.Entry(root)
entry_name.grid(row=0, column=1)
entry_email.grid(row=1, column=1)
entry_course.grid(row=2, column=1)
tk.Button(root, text="Register", command=register).grid(row=3, column=1)
root.mainloop()