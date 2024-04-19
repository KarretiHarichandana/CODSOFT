from tkinter import * 
from tkinter import messagebox 

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x450+500+300')
ws.title('PythonGuides')
ws.config(bg="#223441")
ws.resizable(width=False,height = False)


frame = Frame(ws)
frame.pack(pady = 10)


lb = Listbox(
    frame,width=25,
    height=6,
    font=('arial',18),
    bd=0,
    fg="#595858",
    highlightthickness = 0,
    selectbackground="#c9c7c7",
    activestyle = "none",
)

lb.pack(side=LEFT,fill=BOTH)

task_list = [
    'Doing Exercise',
    'Reading Books',
    'Drinking Water',
    'Cooking Delicious Food'
    'Eating Healthyfood',
    'Learning Something new',
    'Doing Code'

]

for item in task_list:
    lb.insert(END,item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill = BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry (
    ws,
    font = ('times',24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text = ('Add Task'),
    font = ('times 14'),
    bg="#c0f768",
    padx=20,
    pady=10,
    command=newTask
)

addTask_btn.pack(fill=BOTH, expand=True,side=LEFT)

delTask_btn = Button(
    button_frame,
    text = "Delete Task",
    font = ('times 14'),
    bg = "#ff8b61",
    padx=20,
    pady=10,
command = deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True,side=LEFT)

ws.mainloop()


