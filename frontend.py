from tkinter import *
from backend import Database

database = Database("bookstore.db")

#Function for Listbox Select Event
def get_selected_row(event):
        try:
            global selected_row
            index = list1.curselection()[0]
            selected_row = list1.get(index)
            e1.delete(0, END)
            e1.insert(END, selected_row[1])
            e2.delete(0, END)
            e2.insert(END, selected_row[2])
            e3.delete(0, END)
            e3.insert(END, selected_row[3])
            e4.delete(0, END)
            e4.insert(END, selected_row[4])
        except IndexError:
            pass

#Backend Function Wrapper
def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END, row)

def update_command():
    database.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def delete_command():
    database.delete(selected_row[0])
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)
        
#Basic Window
window = Tk()
window.config(bg='#007FFF')
window.resizable(0,0)
window.title("Book Management Software")

#Labels 
l1 = Label(window, text = 'Title', font = 'OpenSans', bg='#007FFF', fg='white')
l1.grid(row=0, column=0)

l2 = Label(window, text = 'Author', font = 'OpenSans', bg='#007FFF', fg='white')
l2.grid(row=0, column=3)

l1 = Label(window, text = 'Year', font = 'OpenSans', bg='#007FFF', fg='white')
l1.grid(row=1, column=0)

l1 = Label(window, text = 'ISBN', font = 'OpenSans', bg='#007FFF', fg='white')
l1.grid(row=1, column=3)

#Entry Widgets
title_text = StringVar()
e1 = Entry(window, font = 'OpenSans', textvariable= title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, font = 'OpenSans', textvariable= author_text)
e2.grid(row=0, column=4, columnspan=2)

year_text = StringVar()
e3 = Entry(window, font = 'OpenSans', textvariable= year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, font = 'OpenSans', textvariable= isbn_text)
e4.grid(row=1, column=4, columnspan=2)

#Buttons
b1 = Button(
    window, 
    text= "View All", 
    width=13, 
    font=('OpensSans',10), 
    bg='#d63031', 
    fg='white',
    command = view_command
)
b1.grid(row=2, column=0, columnspan=2)

b2 = Button(
    window, 
    text= "Search Entry", 
    width=13, 
    font=('OpensSans',10), 
    bg='#d63031', 
    fg = 'white',
    command = search_command
)
b2.grid(row=3, column=0, columnspan=2)

b3 = Button(
    window, 
    text= "Add Entry", 
    width=13, 
    font=('Open Sans',10), 
    bg='#d63031', 
    fg='white',
    command = add_command
)
b3.grid(row=4, column=0, columnspan=2)

b4 = Button(
    window, 
    text= "Update Selected", 
    width=13, 
    font=('OpensSans',10), 
    bg='#d63031', 
    fg='white',
    command = update_command
)
b4.grid(row=5, column=0, columnspan=2)

b5 = Button(
    window, 
    text= "DEL Selected", 
    width=13, 
    font=('OpensSans',10), 
    bg='#d63031', 
    fg='white',
    command = delete_command
)
b5.grid(row=6, column=0, columnspan=2)

b6 = Button(
    window, 
    text= "Close",
    width=13, 
    font=('OpensSans',10), 
    bg='#d63031', 
    fg='white',
    command = window.destroy
)
b6.grid(row=7, column=0, columnspan=2)

#Listbox and Scrollbar
list1 = Listbox(window, height=13, width=40)
list1.grid(row=2, column=3, rowspan=6, columnspan=2)

scbar = Scrollbar(window)
scbar.grid(row=2, column=2, rowspan=5)

list1.config(yscrollcommand = scbar.set)
scbar.config(command = list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()