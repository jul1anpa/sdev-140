'''
File: maketime.py
This program creates a GUI class object that functions as a task list that takes user input
and builds a list of tasks. The user can manipulate the list using command buttons.
'''


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def validate_text(value):
    '''Validates a user's input into the entry widget.'''

    return all(char.isalnum() or char.isspace() for char in value) # Makes sure that a user's input is alphanumeric or words seperated by spaces


class MakeTime():
    '''Represents an instance of a GUI object'''

    def __init__(self, root):
        '''Constructor creates a main window using the provided root variable. 
        It also initiates the creation of widgets, images, and custom parameters.'''

        self.root = root # Represents the main window
        self.icon_image = tk.PhotoImage(file="/Users/julianpayne/Desktop/SDEV 140/Final Project/icon.png") # Stores an image object
        self.root.iconphoto(True, self.icon_image) # Sets program icon image to image object
        self.root.title("Maketime") # Sets title for main window
        self.tasks = [] # Creates an empty list for tasks to be stored
        self.main_frame = tk.Frame(self.root, relief="raised", bd=10, bg="white") # Creates a frame for the main window
        self.main_frame.pack() # Packs frame into the window
        self.create_widgets() # Initializes widgets
        self.create_images() # Initializes images
    
    def create_images(self):
        '''Creates images'''

        # Creates logo image
        self.image = Image.open("/Users/julianpayne/Desktop/SDEV 140/Final Project/logo_with_bg.png") # Stores an image object
        self.width = 400 # Stores a specfied width
        self.length = 150 # Stores a specfied length
        self.image = self.image.resize((self.width, self.length), Image.ANTIALIAS) # Stores a resized image object
        self.tk_image = ImageTk.PhotoImage(self.image) # Uses ImageTk to create a tkinter compatible image object
        self.frame = tk.Frame(self.main_frame) # Creates a frame within the main window frame
        self.frame.grid(row=0, column=0, columnspan=2) # Sets placement for frame
        self.image_label = tk.Label(self.frame, image=self.tk_image) # Creates Label object using the image object
        self.image_label.grid(row=0, column=0, padx=0, pady=0) # Sets placement for label

        # Creates border image using same method as before
        self.image_border = Image.open("/Users/julianpayne/Desktop/SDEV 140/Final Project/wave.png")
        self.image_border = self.image_border.resize((self.width, self.length), Image.ANTIALIAS)
        self.tk_image_border = ImageTk.PhotoImage(self.image_border)
        self.frame_border = tk.Frame(self.main_frame)
        self.frame_border.grid(row=4, column=0, columnspan=2)
        self.image_border_label = tk.Label(self.frame_border, image=self.tk_image_border, background="white")
        self.image_border_label.grid(row=4, column=0, padx=0, pady=0)

    def create_widgets(self):
        '''Creates widgets'''

        # Frame for Create Task Button
        self.entry_frame = tk.Frame(self.main_frame, bg="white") # Creates a frame object
        self.entry_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2) # Sets placement for frame

        # Add Create Task Button
        self.create_button = tk.Button(self.entry_frame, text="Create a new Task here!", command=self.create_task_window, highlightbackground="white") # Creates a button object with command functionality
        self.create_button.pack(side=tk.TOP) # Sets placement for button object

        # Task List Box
        self.task_list = ttk.Treeview(self.main_frame, columns=("Tasks", "Status"), show="headings", height=10) # Creates treeview object
        self.task_list.grid(row=2, column=0, columnspan=2, pady=5) # Sets placement
        self.task_list.heading("Tasks", text="Tasks") # Sets headings
        self.task_list.heading("Status", text="Status")

        # Frame for Delete Task and Mark Completed Buttons
        self.button_frame = tk.Frame(self.main_frame, bg="white") # Creates frame object for buttons
        self.button_frame.grid(row=3, column=0, padx=10, pady=5, columnspan=2) # Sets placement

        # Mark Complete Button
        self.complete_button = tk.Button(self.button_frame, text="Mark as Complete", command=self.mark_complete, highlightbackground="white", foreground="#b0d1a2") # Creates a button object with command functionality
        self.complete_button.pack(side=tk.LEFT, padx=5) # Sets placement

        # Delete Button using same method as above
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, highlightbackground="white", foreground="#aca3cd")
        self.delete_button.pack(side=tk.LEFT, padx=5)


    def add_task(self):
        '''Adds functionality to the add_button widget. Allows a user to add tasks to the
        Treeview widget in the main window.'''

        self.task_text = self.task_entry.get() # Stores the contents of the task entry widget into a variable
        if validate_text(self.task_text): # Makes sure user input passes validation
            if self.task_text.strip(): # Makes sure user input is not blank
                self.tasks.append(self.task_text) # Appends string to tasks list
                self.task_list.insert("", tk.END, values=(self.task_text, "Not Complete")) # Inserts string into treeview object
                self.task_entry.delete(0, tk.END) # Deletes string from task entry object
            else:
                messagebox.showerror("Error", "Task cannot be blank.")
        else:
            messagebox.showerror("Error", "Invalid input. Please enter only alphanumeric characters or spaces.")

    def delete_task(self):
        '''Adds functionality to the delete_button widget. Allows a user to select a task using their
        cursor and press the delete button to delete it from the Treeview widget.'''

        selected_task_indices = self.task_list.selection() # Stores index of user cursor selection
        if selected_task_indices: # Checks if user has selected a task
            for index in reversed(selected_task_indices): # Uses cursor index to remove a selection from the list and treeview object
                self.task_text = self.task_list.item(index)["values"][0]
                self.tasks.remove(self.task_text)
                self.task_list.delete(index)

    def mark_complete(self):
        '''Adds functionality to the complete_button widget. Allows a user to select a task using their cursor
        and press the mark complete button to change the status of the task.'''

        self.selected_task_indices = self.task_list.selection()
        if self.selected_task_indices:
            for item_id in self.selected_task_indices: # Uses the cursor index to check if a task is not marked Complete and changes the status if so
                self.task_item = self.task_list.item(item_id)
                if self.task_item["values"][1] == "Not Complete":
                    self.task_list.item(item_id, values=(self.task_item["values"][0], "Complete"))

    def create_task_window(self):
        '''Creates a new window that allows a user to enter a task.'''

        self.task_window = tk.Toplevel(self.root) # Creates a new top level window
        self.task_window.resizable(False, False) # Prevents user from resizing the window
        self.task_window.title("Task Entry") # Sets a title for the top level window
        self.task_frame = tk.Frame(self.task_window, relief="raised", bd=10, bg="white") # Creates a frame for the window
        self.task_frame.pack() # Sets placement for frame

        # Creates a new image object for the top level window and places it within a frame for window layout
        self.image_border_two = Image.open("/Users/julianpayne/Desktop/SDEV 140/Final Project/wave_2.png")
        self.image_border_two = self.image_border_two.resize((self.width, self.length), Image.ANTIALIAS)
        self.tk_image_border_two = ImageTk.PhotoImage(self.image_border_two)
        self.frame_border_two = tk.Frame(self.task_frame)
        self.frame_border_two.grid(row=0, column=0, columnspan=2)
        self.image_border_label_two = tk.Label(self.frame_border_two, image=self.tk_image_border_two, background="white")
        self.image_border_label_two.grid(row=0, column=0, padx=0, pady=0)

        self.instruction_label = tk.Label(self.task_frame, text="Type in tasks below to add them to your list!") # Creates Label object to provide user instruction
        self.instruction_label.configure(bg="white")
        self.instruction_label.grid(row=1, column=1, padx=10, pady=10)

        self.task_entry = tk.Entry(self.task_frame, width=40, highlightthickness=0) # Creates an entry object
        self.task_entry.grid(row=2, column=1, padx=10)
        self.add_button = tk.Button(self.task_frame, text="Add Task", highlightbackground="white", command=self.add_task) # Creates a button object with command functionality
        self.add_button.grid(row=3, column=1, padx=10, pady=10)



if __name__ == "__main__":
    root = tk.Tk() # Creates the main window object
    root.configure(background="white") # Sets background color of window object
    root.resizable(False, False) # Prevents user from resizing the window
    my_gui = MakeTime(root) # Initializes the MakeTime class using the main window object
    root.mainloop() # Runs the main program loop until program is stopped