from tkinter import *
from tkinter import messagebox
from passwordGenerator import *
import pyperclip
import json

#----data----#

# --------------------SAVE PASSWORD -----------------------#
def saveInfo():
    email = email_input.get()
    password = password_input.get()
    web = website_input.get()
    if not email or not password or not web:
        if not email:
            empty = 'Email is Empty'
        if not password:
            empty = 'Password is Empty'
        if not web:
            empty = 'Website is Empty'
        if (not email) and (not password):
            empty = 'Email and Password are empty'
        if (not password) and (not web):
            empty = 'Password and Website are empty'
        if (not web) and (not email):
            empty = 'Website and Email are empty'
        if (not web) and (not email) and (not password):
            empty = 'Fill Your Email, Website and Password'

        messagebox.showwarning(title='Missing Parameter(s)', message=empty)
    elif email and password and web:
        # ----------------------Creating Pop ups---------------------#
        is_ok = messagebox.askokcancel(title='Save Password 🥷',
                                       message=f'These are the details you entered:\nEmail: {email}\nPassword: {password}\n'
                                               f'Are you sure you want to save this information '
                                               f'for {web} Account?')

        if is_ok:
            new_data = {web: {
                'email': email,
                'password': password
            }}
            try:
                with open('info.json', 'r') as info:
                    data = json.load(info)
            except FileNotFoundError:
                with open('info.json', 'w') as info:
                    json.dump(new_data, info, indent=4)
            else:
                data.update(new_data)
                with open('info.json', 'w') as info:
                    json.dump(data, info, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


def search():
    web = website_input.get()
    with open('info.json', 'r') as info:
        data = json.load(info)
    try:
        file = data[web]
    except KeyError:
        messagebox.showwarning(title=f'Info for {web}', message=f'Opps ! can not find {web} in the database')
    else:
        file_email = file['email']
        file_password = file['password']
        messagebox.showinfo(title=f'Info for {web}', message=f'email :{file_email}\npassword :{file_password}')


def Generator():
    password_input.delete(0, END)
    password_input.insert(0, f'{GeneratePassword()}')
    pyperclip.copy(password_input.get())


# --------------------UI SETUP ------------------#
my_screen = Tk()
my_screen.title('Password Manager 🔐')
my_screen.config(padx=40, pady=40)
my_canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
my_canvas.create_image(100, 100, image=logo)
my_canvas.grid(row=0, column=1)
website_label = Label(text='Website:', fg='white')
website_label.grid(column=0, row=1)
website_input = Entry(bg='white', width=21, fg='black', insertbackground="blue")
website_input.config(cursor='')
website_input.focus()
website_input.grid(column=1, row=1, )
email_label = Label(text='Email/Username:', fg='white')
email_label.grid(row=2, column=0)
email_input = Entry(bg='white', width=38, fg='black', insertbackground="blue")
email_input.insert(0, 'ridwan.rede02@gmail.com')
email_input.grid(column=1, row=2, columnspan=2)
password_label = Label(text='Password:', fg='white')
password_label.grid(column=0, row=3)
password_input = Entry(bg='white', width=21, fg='black', insertbackground="blue")
password_input.grid(column=1, row=3, )

generate_password_button = Button(text='Generate Password', fg='black', bg='white', width=13, command=Generator)
generate_password_button.grid(column=2, row=3)
search_button = Button(text='Search', fg='black', bg='white', width=10,command=search)
search_button.grid(column=2, row=1)
add_button = Button(text='Add', bg='white', fg='black', width=36, command=saveInfo)
add_button.grid(row=4, column=1, columnspan=2, )

my_screen.mainloop()
