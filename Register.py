import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 15)
SMALLFONT =("Verdana", 10)

class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        CREDENTIALS = controller.get_credentials()
        # Labels
        full_name = tk.StringVar()
        name_var = tk.StringVar()
        passw_var = tk.StringVar()
        mobile = tk.StringVar()
        email = tk.StringVar()

        def submit():
            if name_var.get() and passw_var.get() and full_name.get() and mobile.get() and email.get() != "":
                controller.show_frame("Login")
                CREDENTIALS[name_var.get()] = [passw_var.get(), full_name.get(), mobile.get(), email.get()]

            else:
                wrong_input_label.config(text="You must fill all the boxes!")
                

            name_var.set("")
            passw_var.set("")
            full_name.set("")
            mobile.set("")
        
        welcome_label = ttk.Label(self, text ="Registration", font = LARGEFONT)
        welcome_label.grid(column=0, row=0)
        wrong_input_label = ttk.Label(self, text="", font=SMALLFONT)
        wrong_input_label.grid(column=1, row=7)

        full_name_label = tk.Label(self, text='Full name', font=('calibre', 10, 'bold'))

        full_name_entry = tk.Entry(self, textvariable=full_name, font=('calibre', 10, 'normal'))

        mobile_label = tk.Label(self, text='Mobile phone', font=('calibre', 10, 'bold'))

        mobile_entry = tk.Entry(self, textvariable=mobile, font=('calibre', 10, 'normal'))

        email_label = tk.Label(self, text='Email', font=('calibre', 10, 'bold'))

        email_entry = tk.Entry(self, textvariable=email, font=('calibre', 10, 'normal'))

        name_label = tk.Label(self, text='Username', font=('calibre', 10, 'bold'))

        name_entry = tk.Entry(self, textvariable=name_var, font=('calibre', 10, 'normal'))

        passw_label = tk.Label(self, text='Password', font=('calibre', 10, 'bold'))

        passw_entry = tk.Entry(self, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

        sub_btn = tk.Button(self, text='Submit', command=submit)
        go_back_btn = tk.Button(self, text='Go back', command=controller.show_frame("Main"))

        full_name_label.grid(row=1, column=0)
        full_name_entry.grid(row=1, column=1)
        mobile_label.grid(row=2, column=0)
        mobile_entry.grid(row=2, column=1)
        email_label.grid(row=3, column=0)
        email_entry.grid(row=3, column=1)
        name_label.grid(row=4, column=0)
        name_entry.grid(row=4, column=1)
        passw_label.grid(row=5, column=0)
        passw_entry.grid(row=5, column=1)
        sub_btn.grid(row=6, column=1)
        go_back_btn.grid(row=8, column=1)
