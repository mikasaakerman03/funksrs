import tkinter as tk
from tkinter import ttk
from rx.subject import Subject


class ToDoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("FRP To-Do List")

        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(self.root, textvariable=self.task_var)
        self.task_entry.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Добавить задачу")
        self.add_button.pack()

        self.delete_button = ttk.Button(self.root, text="Удалить задачу", command=self.delete_selected_task)
        self.delete_button.pack()

        self.task_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_list.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        #Поток события курамыз
        add_task_subject = Subject()


        self.add_button.bind("<Button-1>", lambda event: add_task_subject.on_next(event))


        add_task_subject.subscribe(lambda event: self.add_task())

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            #Списокка косамыз тапсырманы
            self.tasks.append(task)
            #Виджетка косамыз тапсырманы
            self.task_list.insert(tk.END, task)
            self.task_var.set("")  # Поле ввода тазалаймыз

    def delete_selected_task(self):

        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            # кетиремиз
            del self.tasks[index]
            self.task_list.delete(index)


if _name_ == "_main_":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

#helloworld
