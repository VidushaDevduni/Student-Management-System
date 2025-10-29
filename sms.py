import tkinter as tk
from tkinter import ttk, messagebox


win = tk.Tk()
win.geometry("1000x760")
win.title("Student Management System")
win.configure(background="maroon4")
win.resizable(False, False)


students = []


def clear_fields():
    noentry.delete(0, tk.END)
    nameentry.delete(0, tk.END)
    classentry.delete(0, tk.END)
    sectionentry.delete(0, tk.END)
    conentry.delete(0, tk.END)
    fatherentry.delete(0, tk.END)
    addentry.delete(0, tk.END)
    gender.set("")

def add_student():
    data = (
        noentry.get(),
        nameentry.get(),
        classentry.get(),
        sectionentry.get(),
        conentry.get(),
        fatherentry.get(),
        addentry.get(),
        gender.get()
    )
    if any(not field for field in data):
        messagebox.showerror("Error", "All fields are required!")
        return

    students.append(data)
    refresh_table()
    clear_fields()

def refresh_table():
    stdtable.delete(*stdtable.get_children())
    for student in students:
        stdtable.insert("", tk.END, values=student)

def get_selected_row(event):
    selected = stdtable.focus()
    if not selected:
        return
    values = stdtable.item(selected, "values")
    if not values:
        return
    clear_fields()
    noentry.insert(0, values[0])
    nameentry.insert(0, values[1])
    classentry.insert(0, values[2])
    sectionentry.insert(0, values[3])
    conentry.insert(0, values[4])
    fatherentry.insert(0, values[5])
    addentry.insert(0, values[6])
    gender.set(values[7])

def update_student():
    selected = stdtable.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a record to update.")
        return
    index = stdtable.index(selected)
    students[index] = (
        noentry.get(),
        nameentry.get(),
        classentry.get(),
        sectionentry.get(),
        conentry.get(),
        fatherentry.get(),
        addentry.get(),
        gender.get()
    )
    refresh_table()
    clear_fields()

def delete_student():
    selected = stdtable.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a record to delete.")
        return
    index = stdtable.index(selected)
    students.pop(index)
    refresh_table()
    clear_fields()

# ---------- TITLE ----------
title = tk.Label(win, text="  Student Management System  ", font=("Arial", 25, "bold"))
title.place(x=250, y=10)

# ---------- LEFT FRAME ----------
fram = tk.LabelFrame(win, text="Enter Your Details", bg="pink2", font=15, relief=tk.GROOVE)
fram.place(x=20, y=80, width=350, height=600)

# Entry fields
nolabel = tk.Label(fram, text="No:", font="black")
nolabel.grid(row=0, column=0, padx=2, pady=2)
noentry = tk.Entry(fram, bd=7)
noentry.grid(row=0, column=1, padx=2, pady=2)

namelabel = tk.Label(fram, text="User Name:", font="black")
namelabel.grid(row=1, column=0, padx=2, pady=2)
nameentry = tk.Entry(fram, bd=7)
nameentry.grid(row=1, column=1, padx=2, pady=2)

emaillabel = tk.Label(fram, text="Class:", font="black")
emaillabel.grid(row=2, column=0, padx=2, pady=2)
classentry = tk.Entry(fram, bd=7)
classentry.grid(row=2, column=1, padx=2, pady=2)

Genderlabel = tk.Label(fram, text="Section:", font="black")
Genderlabel.grid(row=3, column=0, padx=2, pady=2)
sectionentry = tk.Entry(fram, bd=7)
sectionentry.grid(row=3, column=1, padx=2, pady=2)

conlabel = tk.Label(fram, text="Contact:", font="black")
conlabel.grid(row=4, column=0, padx=2, pady=2)
conentry = tk.Entry(fram, bd=7)
conentry.grid(row=4, column=1, padx=2, pady=2)

birthlabel = tk.Label(fram, text="Father's Name:", font="black")
birthlabel.grid(row=5, column=0, padx=2, pady=2)
fatherentry = tk.Entry(fram, bd=7)
fatherentry.grid(row=5, column=1, padx=2, pady=2)

addlabel = tk.Label(fram, text="Address:", font="black")
addlabel.grid(row=6, column=0, padx=2, pady=2)
addentry = tk.Entry(fram, bd=7)
addentry.grid(row=6, column=1, padx=2, pady=2)

genderlabel = tk.Label(fram, text="Gender:", font="black")
genderlabel.grid(row=7, column=0, padx=2, pady=2)
gender = ttk.Combobox(fram, values=("Male", "Female"), state="readonly")
gender.grid(row=7, column=1, padx=2, pady=2)

# ---------- BUTTONS ----------
btnf = tk.Frame(fram, relief=tk.GROOVE, bg="pink")
btnf.place(x=10, y=300, width=310, height=245)

tk.Button(btnf, bg="white", fg="black", text="ADD", width=41, height=2, command=add_student).grid(row=2, column=2, padx=7, pady=8)
tk.Button(btnf, bg="white", fg="black", text="UPDATE", width=41, height=2, command=update_student).grid(row=4, column=2, padx=7, pady=8)
tk.Button(btnf, bg="white", fg="black", text="DELETE", width=41, height=2, command=delete_student).grid(row=6, column=2, padx=7, pady=8)
tk.Button(btnf, bg="white", fg="black", text="CLEAR", width=41, height=2, command=clear_fields).grid(row=8, column=2, padx=7, pady=8)

# ---------- RIGHT FRAME ----------
dfram = tk.LabelFrame(win, bg="white", font=15, relief=tk.GROOVE)
dfram.place(x=400, y=80, width=580, height=600)

sframe = tk.Frame(dfram, bg="black", relief=tk.GROOVE)
sframe.pack(side=tk.TOP, fill=tk.X)

tk.Label(sframe, bg="white", relief=tk.GROOVE, width=15, height=1, text="Search", font=12).grid(row=0, column=0, padx=2, pady=2)
com1 = ttk.Combobox(sframe, state="readonly", values=("No", "User Name", "Class", "Section", "Contact", "Father's Name", "Address", "Gender"))
com1.grid(row=0, column=1)
tk.Entry(sframe, width=20).grid(row=0, column=2, padx=6, pady=6)
tk.Button(sframe, text="Search", bg="white", width=15).grid(row=0, column=3, padx=6, pady=6)
tk.Button(sframe, text="Show All", bg="white", width=15, command=refresh_table).grid(row=0, column=4, padx=6, pady=6)

# ---------- TABLE ----------
tblfram = tk.Frame(dfram, bg="pink", relief=tk.GROOVE)
tblfram.pack(fill=tk.BOTH, expand=True)

x = tk.Scrollbar(tblfram, orient=tk.HORIZONTAL)
y = tk.Scrollbar(tblfram, orient=tk.VERTICAL)

stdtable = ttk.Treeview(tblfram, columns=("No", "User Name", "Class", "Section", "Contact", "Father's Name", "Address", "Gender"),
                        yscrollcommand=y.set, xscrollcommand=x.set)

y.config(command=stdtable.yview)
y.pack(side=tk.RIGHT, fill=tk.Y)
x.config(command=stdtable.xview)
x.pack(side=tk.BOTTOM, fill=tk.X)

for col in ("No", "User Name", "Class", "Section", "Contact", "Father's Name", "Address", "Gender"):
    stdtable.heading(col, text=col)
    stdtable.column(col, width=100)

stdtable.pack(fill=tk.BOTH, expand=True)
stdtable.bind("<ButtonRelease-1>", get_selected_row)

win.mainloop()
