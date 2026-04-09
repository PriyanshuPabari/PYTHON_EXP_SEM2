import tkinter as tk
def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
expression = ""
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=8, relief=tk.RIDGE, justify='right')
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 14", height=2)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)
root.mainloop()