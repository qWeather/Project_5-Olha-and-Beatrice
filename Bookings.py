import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 15)
SMALLFONT = ("Veredana", 10)
SELECTED_SHOWS = {}
SEATS_CHECKBOXES = {}
SELECTED_SEATS = []
class Bookings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        AVAILABLE_SHOWS = controller.get_shows()

        # Labels
        logout_label = ttk.Label(self, text="List of Shows", font=LARGEFONT)
        logout_label.grid(column=0, row=0)

        # Table View

        columns = ('show_name', 'date', 'time', 'no_seats', 'description')

        shows_treeview = ttk.Treeview(self, columns=columns, show='headings')

        shows_treeview.heading('show_name', text='Name')
        shows_treeview.heading('date', text='Date')
        shows_treeview.heading('time', text='Time')
        shows_treeview.heading('no_seats', text='Available Seats')
        shows_treeview.heading('description', text='Description')

        shows_treeview.column('show_name', width=100, anchor=tk.W)
        shows_treeview.column('date', width=100, anchor=tk.W)
        shows_treeview.column('time', width=100, anchor=tk.W)
        shows_treeview.column('no_seats', width=100, anchor=tk.W)
        shows_treeview.column('description', width=100, anchor=tk.W)

        for key, value in AVAILABLE_SHOWS.items():
            temp = value
            temp.insert(0, key)
            SELECTED_SHOWS[key] = value[-1]
            shows_treeview.insert('', tk.END, values=temp)

        def get_selected_shows(self):
            return SELECTED_SHOWS

        # Buttons
        next_btn = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame("Seats"))
        next_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Dashboard"))
        go_back_btn.grid(row=3, column=1)


class Seats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        AVAILABLE_SEATS = controller.get_seats()
        SELECTED_SHOWS = controller.get_selected_shows()

        # Labels
        logout_label = ttk.Label(
            self, text="List of Available Seats", font=LARGEFONT)
        logout_label.grid(column=0, row=0)

        # Checkboxes
        i = 2
        checked = tk.IntVar()
        for key, value in AVAILABLE_SEATS.items():
            if value == "available":
                seat_checkbox = ttk.Checkbutton(self, text=key, var=checked)
                SEATS_CHECKBOXES[key] = checked.get()
                seat_checkbox.grid(row=i, sticky=tk.W)
                i += 1

        def collect_checked():
            for key, value in SEATS_CHECKBOXES.items():
                if value == 1:
                    SELECTED_SEATS.append(key)
            return key

        def collect_shows_price():
            total_price = 0
            for key, value in SELECTED_SHOWS.items():
                total_price += value * len(SELECTED_SEATS)
            return key, total_price

        # Buttons
        next_btn = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame("Summary"))
        next_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Bookings"))
        go_back_btn.grid(row=3, column=1)


class Summary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        logout_label = ttk.Label(self, text="Summary", font=LARGEFONT)
        logout_label.grid(column=0, row=0)

        show_details_label = ttk.Label(
            self, text="Show Details: ", font=LARGEFONT)
        show_details_label.grid(column=0, row=1)

        seats_label = ttk.Label(self, text="Seat/s", font=LARGEFONT)
        seats_label.grid(column=1, row=1)

        details_label = ttk.Label(
            self, text=controller.collect_shows_price(), font=LARGEFONT)
        details_label.grid(column=0, row=2)

        label = ttk.Label(
            self, text=controller.collect_checked(), font=LARGEFONT)
        label.grid(column=1, row=2)

        # Buttons
        pay_btn = ttk.Button(
            self, text="Pay", command=lambda: controller.show_frame("Dashboard"))
        pay_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Seats"))
        go_back_btn.grid(row=3, column=1)
