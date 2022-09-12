import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 15)

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # Labels
        logout_label = ttk.Label(self, text ="Log out!", font = LARGEFONT)
        logout_label.grid(column=0, row=0)

        # Buttons
        logout_btn = ttk.Button(self, text ="Book a Show", command = lambda : controller.show_frame("Bookings"))
        logout_btn.grid(row = 2, column = 1)
        logout_btn = ttk.Button(self, text ="Cancel a Booking", command = lambda : controller.show_frame("Cancel"))
        logout_btn.grid(row = 3, column = 1)
        logout_btn = ttk.Button(self, text ="Show ", command = lambda : controller.show_frame("Reservations"))
        logout_btn.grid(row = 4, column = 1)
        logout_btn = ttk.Button(self, text ="Logout", command = lambda : controller.show_frame("Main"))
        logout_btn.grid(row = 5, column = 1)