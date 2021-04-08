from tkinter import *

root = Tk()
root.title('Password Generator')
root.geometry("350x250")


password_menu = [
    ("password containing 8 characters", 8),
    ("password containing 16 characters", 16),
    ("password containing 32 characters", 32),
]

#default value for password lenhth 
default_password_length = IntVar()
default_password_length.set(8)

for menu_info, password_length in password_menu:
    menu_buttons = Radiobutton(root, text=menu_info, variable=default_password_length, value=password_length)
    menu_buttons.grid()


import random
from string import digits, punctuation,ascii_letters

def password_generator(password_length):
    entry_field.delete(0, END)
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols)for i in range(password_length))
    entry_field.insert(0, password)# 0 mean position

def copy_generated_password():
    copied_password = entry_field.get ()
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(copied_password) # copying to the clipboard
    

button = Button(root, text="Get password!",command=lambda: password_generator(default_password_length.get()))
button.grid()

entry_field = Entry(root,width=45)
entry_field.grid(row=4, column=0)

copy_button = Button(root, text = "Copy Password!", command = copy_generated_password)
copy_button.grid(row=5, column=0)

root.mainloop()