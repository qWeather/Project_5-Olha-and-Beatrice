import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 15)
SMALLFONT = ("Veredana", 10)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        CREDENTIALS = controller.get_credentials()

        # Login Verification
        def login():
            for username, password in CREDENTIALS.items():
                if username == username_entry.get() and password[0] == password_entry.get():
                    controller.show_frame("Dashboard")
                    break
                else:
                    wrong_input_label.config(text="Login details don't match!")
        # Labels
        username_label = ttk.Label(self, text="Username: ", font=SMALLFONT)
        username_label.grid(column=0, row=1)
        password_label = ttk.Label(self, text="Password", font=SMALLFONT)
        password_label.grid(column=0, row=2)
        wrong_input_label = ttk.Label(self, text="", font=SMALLFONT)
        wrong_input_label.grid(column=0, row=3)

        # Text Fields
        username_input = tk.StringVar()
        password_input = tk.StringVar()

        username_entry = ttk.Entry(
            self, textvariable=username_input, font=('calibre', 10, 'normal'))
        username_entry.grid(row=1, column=1)
        password_entry = ttk.Entry(
            self, textvariable=password_input, font=('calibre', 10, 'normal'))
        password_entry.grid(row=2, column=1)

        # Buttons
        login_btn = ttk.Button(self, text="Login", command=login)
        login_btn.grid(row=4, column=0)
