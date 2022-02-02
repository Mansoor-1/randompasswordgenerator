import random

import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo


def low():
    entry.delete(0, END)

    length = var1.get()

    if length == 0:
        show_msg()
    else:
        Random_password.config(text="")
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + lower
        digits = upper + "0123456789 !@#$%^&*()"
        password = ""

        if var.get() == 0:
            for i in range(0, length):
                password = password + random.choice(lower)
            return password

        elif var.get() == 1:
            for i in range(0, length):
                password = password + random.choice(upper)
            return password

        elif var.get() == 3:
            for i in range(0, length):
                password = password + random.choice(digits)
            return password
        else:
            show_msg()


def show_msg():
    return Random_password.config(text="Please Choose Password length First!")


def generate():
    password1 = low()
    entry.insert(10, password1)
    msg = "Congratulations! Password Created Successfully"
    Random_password.config(text=msg)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


def viewSelected():
    choice = var.get()

    if choice == 1:
        output = "Password will be generated containing alphabets in lower case"

    elif choice == 0:
        output = "Password will be combination of Upper case and lowercase alphabets"

    elif choice == 3:
        output = "Password will be combination of alphabets, numbers and special characters"

    else:
        output = "Invalid selection"

    return info_label.config(text=output)


def reset():
    entry.delete(0, END)
    info_label.config(text="")
    Random_password.config(text="")
    combo.set(0)
    var.set(0)


def clear():
    entry.delete(0, END)
    Random_password.config(text="")


root = Tk()
var = IntVar()
var1 = IntVar()

root.geometry("830x550")
root.resizable(False, False)
root.title("Random Password Generator")
root.config(bg="#15153a")

# main heading
Random_password1 = Label(root, text="Random Password Generator", font=("Helvetica", 30, "bold"), foreground="#fb743e",
                        background="#15153a")
Random_password1.place(x=130, y=15)

# select length of password
c_label = Label(root, text="I want a password with ", font=("Arial", 13), foreground="white", background="#15153a")
c_label.grid(row=1)
c_label.place(x=200, y=104)

# combobox for selecting length
combo = Combobox(root, background="#363c53", textvariable=var1)

combo['values'] = (0, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)

combo['state'] = 'readonly'


def length_changed(event):
    """ handle the length changed event """
    showinfo(
        title='Password Length',
        message=f'Your Password will be {var1.get()} characters long'
    )


combo.bind('<<ComboboxSelected>>', length_changed)
combo.place(x=380, y=104)
combo.current(0)

c_label = Label(root, text="characters", font=("Arial", 13), foreground="white", background="#15153a")
c_label.grid(row=1)
c_label.place(x=530, y=104)

radio_label = Label(root, text="Select Password Type: ", font=("Arial", 12), foreground="white", background="#15153a")
radio_label.grid(row=1)
radio_label.place(x=200, y=140)

# radio buttons for options
radio_low = Radiobutton(root, text="Low", variable=var, value=0, command=viewSelected)
radio_low.grid(row=1, column=2, sticky='E')
radio_low.place(x=350, y=170)

radio_middle = Radiobutton(root, text="Medium", variable=var, value=1, command=viewSelected)
radio_middle.grid(row=1, column=3, sticky='E')
radio_middle.place(x=400, y=170)

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3, command=viewSelected)
radio_strong.grid(row=1, column=4, sticky='E')
radio_strong.place(x=475, y=170)

# information about options
info_label = Label(root, text=" ", font=("Times", "15", "bold italic"), foreground="#7edcea", background="#15153a")
info_label.grid(row=1)
info_label.place(x=80, y=200)

# generate password button

generate_button = Button(root, text="Generate Password", width=30, command=generate)
generate_button.grid(row=0, column=3)
generate_button.place(x=350, y=290)

Random_password = Label(root, text="", font=("Arial", 16, "bold italic"), foreground="#fb743e", background="#15153a")
Random_password.place(x=200, y=350)

entry = Entry(root, width=50)
entry.grid(row=0, column=1)
entry.place(x=290, y=400)

copy_button = Button(root, text="Copy", width=7, command=copy1)
copy_button.grid(row=0, column=1)
copy_button.place(x=370, y=450)

reset_button = Button(root, text="Reset", width=7, command=reset)
reset_button.grid(row=0, column=1)
reset_button.place(x=420, y=450)

clear_button = Button(root, text="Clear", width=7, command=clear)
clear_button.grid(row=0, column=1)
clear_button.place(x=470, y=450)

root.mainloop()
