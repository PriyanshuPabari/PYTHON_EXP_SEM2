import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()
def signup():
    user = entry_user.get()
    pwd = entry_pass.get()

    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (user, pwd))
        conn.commit()
        messagebox.showinfo("Success", "Account Created")
    except:
        messagebox.showerror("Error", "User already exists")
def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")
root = tk.Tk()
root.title("Login System")
tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Password").grid(row=1, column=0)
entry_user = tk.Entry(root)
entry_pass = tk.Entry(root, show="*")
entry_user.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)
tk.Button(root, text="Signup", command=signup).grid(row=2, column=0)
tk.Button(root, text="Login", command=login).grid(row=2, column=1)
root.mainloop()