import tkinter as tk
from tkinter import ttk


# Login Class
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        CREDENTIALS = controller.get_credentials()
        # CURRENT_USERNAME = ""
        # Vars
        username_var = tk.StringVar()
        password_var = tk.StringVar()

        # Login Verification
        def login():
            for username, password in CREDENTIALS.items():
                if username == username_var.get() and password[0] == password_var.get():
                    controller.set_curr_user(username)
                    controller.show_frame("Dashboard")
                    # CURRENT_USERNAME = username
                    break
                else:
                    wrong_input_label.config(text="Login details don't match!")

            username_var.set("")
            password_var.set("")

        # Labels
        welcome_label = ttk.Label(self, text="Login", font=('verdana', 15, 'bold')).grid(row=0, column=0)
        username_label = ttk.Label(self, text="Username: ", font=('verdana', 10, 'bold')).grid(row=1, column=0)
        password_label = ttk.Label(self, text="Password: ", font=('verdana', 10, 'bold')).grid(row=2, column=0)
        wrong_input_label = ttk.Label(self, text="", font=('verdana', 10, 'bold'))
        wrong_input_label.grid(column=1, row=3)

        # Text Fields
        username_entry = ttk.Entry(self, textvariable=username_var, font=('calibre', 10, 'normal')).grid(row=1,
                                                                                                         column=1)
        password_entry = ttk.Entry(self, textvariable=password_var, font=('calibre', 10, 'normal'), show='*').grid(
            row=2, column=1)

        # Buttons
        login_btn = ttk.Button(self, text="Login", width=20, command=login).grid(row=4, column=1)
        go_back_btn = ttk.Button(self, text="Go back", width=20, command=lambda: controller.show_frame("Main")).grid(
            row=5, column=1)


# Register Class
class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        CREDENTIALS = controller.get_credentials()

        # Vars
        full_name = tk.StringVar()
        name_var = tk.StringVar()
        passw_var = tk.StringVar()
        mobile = tk.StringVar()
        email = tk.StringVar()

        # Format Email
        def format_email(email):
            if len(email.split("@")[0]) < 1 or email.count(".") != 1 or email.count("@") != 1 or \
                    (not email.endswith(".co") and not email.endswith(".com") and not email.endswith(
                        ".in") and not email.endswith(".org")):
                return False
            else:
                return True

        # Register Details
        def submit():
            if name_var.get() and passw_var.get() and full_name.get() and mobile.get() and email.get() == "":
                wrong_input_label.config(text="You must fill all the boxes!")
            elif len(passw_var.get()) < 8:
                wrong_input_label.config(text="Password must have a minimum of 8 characters!")
            elif len(mobile.get()) < 11 and mobile.get().isdigit():
                wrong_input_label.config(text="Mobile number format incorrect!")
            elif not format_email(email.get()):
                wrong_input_label.config(text="Email format incorrect!")
            else:
                controller.show_frame("Login")
                CREDENTIALS[name_var.get()] = [passw_var.get(), full_name.get(), mobile.get(), email.get()]

            name_var.set("")
            passw_var.set("")
            full_name.set("")
            mobile.set("")

        # Labels
        welcome_label = ttk.Label(self, text="Registration", font=('verdana', 15, 'bold')).grid(column=0, row=0)
        wrong_input_label = ttk.Label(self, text="", font=('verdana', 10, 'bold'))
        wrong_input_label.grid(column=1, row=7)

        # Textfields
        full_name_label = ttk.Label(self, text='Full name: ', font=('verdana', 10, 'bold')).grid(row=1, column=0)
        full_name_entry = ttk.Entry(self, textvariable=full_name, font=('verdana', 10, 'normal')).grid(row=1, column=1)
        mobile_label = ttk.Label(self, text='Mobile Phone: ', font=('verdana', 10, 'bold')).grid(row=2, column=0)
        mobile_entry = ttk.Entry(self, textvariable=mobile, font=('verdana', 10, 'normal')).grid(row=2, column=1)
        email_label = ttk.Label(self, text='Email: ', font=('verdana', 10, 'bold')).grid(row=3, column=0)
        email_entry = ttk.Entry(self, textvariable=email, font=('verdana', 10, 'normal')).grid(row=3, column=1)
        name_label = ttk.Label(self, text='Username: ', font=('verdana', 10, 'bold')).grid(row=4, column=0)
        name_entry = ttk.Entry(self, textvariable=name_var, font=('verdana', 10, 'normal')).grid(row=4, column=1)
        passw_label = ttk.Label(self, text='Password: ', font=('verdana', 10, 'bold')).grid(row=5, column=0)
        passw_entry = ttk.Entry(self, textvariable=passw_var, font=('verdana', 10, 'normal'), show='*').grid(row=5,
                                                                                                             column=1)

        sub_btn = ttk.Button(self, text='Submit', command=submit).grid(row=6, column=1)
        go_back_btn = ttk.Button(self, text='Back', command=lambda : controller.show_frame("Main")).grid(row=8, column=1)