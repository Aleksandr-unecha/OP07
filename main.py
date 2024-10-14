import tkinter as tk

def greet():
    name = entry.get()
    greeting_label.config(text=f"Привет, {name}!")

root = tk.Tk()
root.title("Приветственное приложение")

label = tk.Label(root, text="Введите ваше имя:")
label.pack()

entry = tk.Entry(root)
entry.pack()

greet_button = tk.Button(root, text="Поприветствовать", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()