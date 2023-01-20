# Arguments with Default Values
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(1)


# Unlimited Arguments *args - TUPLE
# def add(*args):
#     print(args[0])
#     sum_num = 0
#     for n in args:
#         sum_num += n
#     return sum_num
# print(add(3, 4, 7, 1))


# **kwargs Many Keyworded Arguments - DICT
# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#
#
# calculate(add=3, multiply=5)
# ----------------------
# def calculate(n, **kwargs):
#     print(kwargs)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(99, add=3, multiply=5)
# ------------------------------------
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)
# print(my_car.color)


# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
#
# bar(1, 2)


# ------------------------------------------



# -------------------------------------------

# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()










# import tkinter
#
# window = tkinter.Tk()
# window.title("GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# # Label
# my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# # How component laid
# # my_label.place(x=50, y=0)
# my_label.grid(column=0, row=0)
# my_label.config(padx=30, pady=30)
#
# # my_label["text"] = "New Text"
# my_label.config(text="New Text2")
#
#
# # Button
# def button_clicked():
#     my_label.config(text=input.get())
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# # 2nd Button
# next_button = tkinter.Button(text="New Button", command=button_clicked)
# next_button.grid(column=2, row=0)
#
# # Entry
# input = tkinter.Entry(width=10)
# # input.pack()
# input.grid(column=3, row=2)
#
# window.mainloop()








import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(pady=50)

# Label
my_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)
my_label.config(padx=50)

# Miles Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

# Entry Filed
input = tkinter.Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

# Result Label
result = tkinter.Label(text="0", font=("Arial", 12, "bold"))
result.grid(column=1, row=1)

# Km Label
km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# Button
def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=f"{km}")



button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()


