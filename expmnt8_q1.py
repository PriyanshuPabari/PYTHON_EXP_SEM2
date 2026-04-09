import tkinter as tk

root = tk.Tk()
root.title("MY FIRST GUI")
root.geometry("400x400")

label = tk.Label(root, text="Hello Welcome To Tkinter", font=("Bold", 16))
label.pack(pady=20)

root.mainloop()