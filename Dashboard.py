import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 15)

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def log_out():
            controller.set_curr_user("")
            controller.show_frame("Main")

        # Labels
        dashboard_label = ttk.Label(self, text =f"Welcome back, {controller.get_curr_user()}!",
                                    font=('verdana', 15, 'bold'))
        dashboard_label.grid(column=0, row=0)

        # Buttons
        logout_btn = ttk.Button(self, text ="Book a Show", command = lambda : controller.show_frame("Bookings"))
        logout_btn.grid(row = 2, column = 1)
        logout_btn = ttk.Button(self, text ="Manage Booking", command = lambda : controller.show_frame("UserBookings"))
        logout_btn.grid(row = 3, column = 1)
        logout_btn = ttk.Button(self, text ="Logout", command = lambda : log_out())
        logout_btn.grid(row = 5, column = 1)