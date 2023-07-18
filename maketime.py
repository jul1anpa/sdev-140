import tkinter as tk

# Define a class which stores self along with its attributes and all functions associated
# with it
class MyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Make Time")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(self.root, width=40, height=10, selectbackground="lightblue")
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text.strip():
            self.tasks.append(task_text)
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.task_list.delete(index)

    def mark_complete(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task_text = self.task_list.get(index)
            if not task_text.startswith("✓ "):
                self.tasks[index] = "✓ " + task_text
                self.task_list.delete(index)
                self.task_list.insert(index, self.tasks[index])



if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MyGUI(root)
    root.mainloop()