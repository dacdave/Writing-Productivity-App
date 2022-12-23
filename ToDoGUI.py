import tkinter as TK
from tkinter import ttk
import datetime as dt
import ToDoBackend

def add():
    add_window = TK.Toplevel(window)
    add_window.title("Add new goal")
    add_window.geometry("400x200+1000+300")

    goal_name = TK.Label(add_window, text="Name")
    goal_name.grid(row=0, column=0)
    goal_date = TK.Label(add_window, text="Due Date")
    goal_date.grid(row=0, column=2)
    goal_status = TK.Label(add_window, text="Status")
    goal_status.grid(row=1, column=0)

    new_goal = TK.StringVar()
    new_goal_entry = TK.Entry(add_window, textvariable=new_goal)
    new_goal_entry.grid(row=0, column=1)
    goal_date = TK.StringVar() #Need to alter this so it stores a date and not a text string
    goal_date_entry = TK.Entry(add_window, textvariable=goal_date)
    goal_date_entry.grid(row=0, column=3)
    goal_status = TK.StringVar() #change to use Booleanvar so can track completion better
    goal_status_entry = TK.Entry(add_window, textvariable=goal_status)
    goal_status_entry.grid(row=1, column=1)

    def create():
        ToDoBackend.insert(
            new_goal.get(),
            goal_date.get(),
            goal_status.get()
        )
        new_goal_entry.delete(0, "end")
        goal_date_entry.delete(0,"end")
        goal_status_entry.delete(0,"end")
        add_window.destroy()
    
    exit = TK.Button(add_window, text="Cancel", width=8, command=add_window.destroy)
    exit.grid(row=3, column=3, padx=5)

    submit = TK.Button(add_window, text="Submit", width=12, command=create)
    submit.grid(row=3, column=2, padx=5)

def clear_display():
    for item in ToDolist.get_children():
        ToDolist.delete(item)

def view():
    clear_display()
    for item in ToDoBackend.goal:
        ToDolist.insert(parent="", index="end", iid=0, text="", values=item)

def delete(): #Can't locate item...probably related to using list instead of structured data
    selected = ToDolist.focus()
    ToDoBackend.goal.remove(selected)

window = TK.Tk()
window.title("To-Do App")
window.geometry("800x550+800+200")

base_pane = TK.PanedWindow(bd=4, relief="raised")
base_pane.pack(fill="both", expand=1)

display_pane = TK.PanedWindow(base_pane, orient="vertical", bd=4, relief="sunken", width=680, height=550)
display_frame = TK.LabelFrame(display_pane, text="To-Do List", padx=5, pady=5)
button_frame = TK.LabelFrame(base_pane, text="", padx=5, pady=5)
base_pane.add(display_pane)
base_pane.add(button_frame)
display_pane.add(display_frame)

ToDo_font = ("Times", "12")
columns = ("ID", "ToDo Item", "Date", "Status")
style = ttk.Style()
style.configure("myStyle.Treeview", bd=0, font=ToDo_font)
style.configure("myStyle.Treeview.Heading", font=ToDo_font)
style.layout("myStyle.Treeview", [("myStyle.Treeview.treearea",{"sticky": "nswe"})])

ToDolist = ttk.Treeview(display_frame, style="myStyle.Treeview", columns=columns, show="headings")
ToDolist.column("#0", width=0, stretch="No")
ToDolist.column("ID", anchor="w", width=40, minwidth=25)
ToDolist.column("ToDo Item", anchor="w", width=180, minwidth=25)
ToDolist.column("Date", anchor="w", width=120, minwidth=25)
ToDolist.column("Status", anchor="w", width=40, minwidth=25)
ToDolist.heading("#0", text="", anchor="w")
ToDolist.heading("ID", text="ID", anchor="w")
ToDolist.heading("ToDo Item", text="ToDo Item", anchor="w")
ToDolist.heading("Date", text="Due Date", anchor="w")
ToDolist.heading("Status", text="Status", anchor="w")
ToDolist.pack(side="left", fill="both", expand=True)
ToDolist["selectmode"] = "browse"

scroller = TK.Scrollbar(display_frame, orient="vertical")
scroller.pack(side="right", fill="y")

ToDolist.configure(yscrollcommand=scroller.set)
scroller.configure(command=ToDolist.yview)

add_button = TK.Button(button_frame, text="Add Goal", width=12, command=add)
add_button.grid(row=2, column=1, padx=5, pady=10)
delete_button = TK.Button(button_frame, text="Delete Goal", width=12, command=delete)
delete_button.grid(row=3, column=1, padx=5, pady=10)
modify_button = TK.Button(button_frame, text="Update Goal", width=12, command=add)
modify_button.grid(row=4, column=1, padx=5, pady=10)
view_button = TK.Button(button_frame, text="View Goals", width=12, command=view)
view_button.grid(row=5, column=1, padx=5, pady=10)
complete_button = TK.Button(button_frame, text="View Completed", width=12, command=add)
complete_button.grid(row=6, column=1, padx=5, pady=10)
close_button = TK.Button(button_frame, text="Close Program", width=12, command=window.destroy)
close_button.grid(row=7, column=1, padx=5, pady=10)

window.mainloop()