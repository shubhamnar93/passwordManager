import json
from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
from  password_manager import PasswordManager
from password_search import PasswordSearcher


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_clicked():
    password = PasswordGenerator.generate_password()
    password_entered.delete(0, END)
    password_entered.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():
    if len(website.get()) <= 0 or len(email.get()) <= 0 or len(password_entered.get()) <= 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any space empty")
    else:
        PasswordManager.save_password(website.get(), email.get(), password_entered.get())
        website.delete(0, 'end')
        password_entered.delete(0, 'end')
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_clicked():
    data = PasswordSearcher.search_password(website.get())
    if data:
        messagebox.showinfo(title=website.get(), message=f"Email: {data['Email']}\nPassword: {data['Password']}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(pady=50, padx=50, bg='white')


photo=PhotoImage(file='logo.png')
canvas=Canvas(width=200, height=200, highlightthickness=0, bg='white')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, sticky=W)


Label(text="Website:", highlightthickness=0, bg='white').grid(column=0, row=1)
Label(text="Email/Username:", highlightthickness=0, bg='white').grid(column=0, row=2)
Label(text="Password:", highlightthickness=0, bg='white').grid(column=0, row=3)


website=Entry(width=30,highlightthickness=1)
website.grid(column=1, row=1, columnspan=2, sticky=W, pady=5)
website.focus()


email=Entry(width=51,highlightthickness=1)
email.grid(column=1, row=2, columnspan=2, sticky=W, pady=5)
email.insert(0,"xyz@email.com")


password_entered=Entry(width=30, highlightthickness=1)
password_entered.grid(column=1, row=3, sticky=W, pady=5)


Button(text="Search", highlightthickness=0, bg='white', width=15, command=search_clicked).grid(row=1, column=2)
Button(text="Generate Password", highlightthickness=0, bg='white', command=generator_clicked).grid(column= 2, row=3, sticky=W)
Button(text='Add',width=43, highlightthickness=0, bg='white', command=add_clicked).grid(column=1, row=4, columnspan=2, sticky=W)
window.mainloop()


