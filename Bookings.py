import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 15)
SMALLFONT = ("Veredana", 10)
SELECTED_SHOWS = {}
<<<<<<< Updated upstream
SEATS_CHECKBOXES = {}
SELECTED_SEATS = []
=======
SEATS_CHECKBOXES = []
SELECTED_SEATS = []
PRICE = 0


>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
        for key, value in AVAILABLE_SHOWS.items():
            temp = value
            temp.insert(0, key)
            SELECTED_SHOWS[key] = value[-1]
=======
        for key, value in self.AVAILABLE_SHOWS.items():
            temp = [key]
            temp.extend(value)
            # SELECTED_SHOWS[key] = float(value[-1][1:])
>>>>>>> Stashed changes
            shows_treeview.insert('', tk.END, values=temp)

        def get_selected_shows(self):
            return SELECTED_SHOWS

        # Buttons
        next_btn = ttk.Button(
            self, text="Next", command=lambda: self.get_shows_and_show_frame(shows_treeview))
        next_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Dashboard"))
        go_back_btn.grid(row=3, column=1)

    def get_shows_and_show_frame(self, shows_treeview):
        item = self.selected_item(shows_treeview)
        SELECTED_SHOWS[item["values"][0]] = float(item["values"][-1][1:])
        self.controller.show_frame("Seats")

    def selected_item(self, shows_treeview):
        curItem = shows_treeview.focus()
        return shows_treeview.item(curItem)


class Seats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
<<<<<<< Updated upstream

        AVAILABLE_SEATS = controller.get_seats()
        SELECTED_SHOWS = controller.get_selected_shows()
=======
        self.AVAILABLE_SEATS = controller.get_seats()
        self.BOOKINGS = controller.get_bookings()
        self.controller = controller
>>>>>>> Stashed changes

        # Labels
        logout_label = ttk.Label(
            self, text="List of Available Seats", font=LARGEFONT)
        logout_label.grid(column=0, row=0)

        # Checkboxes
        i = 2
        checked = tk.IntVar()
        for key, value in AVAILABLE_SEATS.items():
            if value == "available":
<<<<<<< Updated upstream
                seat_checkbox = ttk.Checkbutton(self, text=key, var=checked)
                SEATS_CHECKBOXES[key] = checked.get()
=======
                checked = tk.StringVar()
                seat_checkbox = ttk.Checkbutton(self, text=key, variable=checked, onvalue=key, offvalue="")
                SEATS_CHECKBOXES.append(checked)
>>>>>>> Stashed changes
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
            self, text="Next", command=lambda: self.do_calcs_and_call_summary())
        next_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Bookings"))
        go_back_btn.grid(row=3, column=1)

<<<<<<< Updated upstream

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
=======
    def open_popup(self):
        pay_win = tk.Toplevel()
        pay_win.geometry("500x500")
        pay_win.title("Griffin Show - Booking Summary")
        pay_win['bg'] = '#5D8A82'
        pay_win.resizable(False, False)
        # Labels
        ttk.Label(pay_win, text="Summary", font=('verdana', 15, 'bold')).grid(column=1, row=0)
        ttk.Label(pay_win, text="Show Details: ", font=('verdana', 10, 'bold')).grid(column=0,row=1)
        ttk.Label(pay_win, text="Seat/s", font=('verdana', 10, 'bold')).grid(column=1, row=1)
        ttk.Label(pay_win, text="Price: ", font=('verdana', 10, 'bold')).grid(column=2, row=1)

        show_name_label = ttk.Label(pay_win, text=self.get_show_name(), font=('verdana', 10, 'normal'))
        show_name_label.grid(column=0, row=2)
        ttk.Label(pay_win, text=self.collect_checked(), font=('verdana', 10, 'normal')).grid(column=1, row=2)

        ttk.Label(pay_win, text=self.collect_shows_price(), font=('verdana', 10, 'normal')).grid(column=2, row=2)

        ttk.Label(self, text="").grid(row=3, column=0)
        pay_btn = ttk.Button(
            pay_win, text="Confirm", command=lambda: self.store_booking_and_go_to_dashboard(pay_win))
        pay_btn.grid(row=6, column=1)
        go_back_btn = ttk.Button(
            pay_win, text="Go back", command=lambda: self.controller.show_frame("Seats"))
        go_back_btn.grid(row=7, column=1)

    def store_booking_and_go_to_dashboard(self, pay_win):
        global SELECTED_SHOWS, SEATS_CHECKBOXES, SELECTED_SEATS, PRICE
        if self.controller.get_curr_user() in self.BOOKINGS.keys():
            self.BOOKINGS[self.controller.get_curr_user()]\
                .append([self.get_show_name(), self.collect_shows_price(), SELECTED_SEATS])
        else:
            self.BOOKINGS[self.controller.get_curr_user()] = \
                [[self.get_show_name(), self.collect_shows_price(), SELECTED_SEATS]]
        SELECTED_SHOWS = {}
        SEATS_CHECKBOXES = []
        self.change_statuses()
        SELECTED_SEATS = []
        PRICE = 0
        pay_win.destroy()
        self.controller.show_frame("Dashboard")


    def do_calcs_and_call_summary(self):
        self.open_popup()

    def get_show_name(self):
        show_name = ""
        for name in SELECTED_SHOWS:
            show_name = name
        return show_name

    @staticmethod
    def collect_checked():
        for value in SEATS_CHECKBOXES:
            if value.get() != "":
                SELECTED_SEATS.append(value.get())
        return len(SELECTED_SEATS)

    @staticmethod
    def collect_shows_price():
        val = 0
        for value in SELECTED_SHOWS.values():
            val = value
        return val * len(SELECTED_SEATS)

    def change_statuses(self):
        seats = self.controller.get_seats()
        for seat in seats.keys():
            if seat in SELECTED_SEATS:
                seats[seat] = "occupied"
>>>>>>> Stashed changes
