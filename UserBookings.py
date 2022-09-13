import tkinter as tk
from tkinter import ttk


class UserBookings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.curr_user = controller.get_curr_user()
        self.USER_BOOKINGS = "" if self.curr_user == "" else controller.get_bookings()[self.curr_user]
        self.AVAILABLE_SHOWS = controller.get_shows()

        # Labels
        logout_label = ttk.Label(self, text="List of Bookings", font=('verdana', 15, 'bold'))
        logout_label.grid(column=0, row=0)

        # Table View

        columns = ('show_name', 'date', 'time', 'price', 'seats')

        bookings_treeview = ttk.Treeview(self, columns=columns, show='headings')

        bookings_treeview.heading('show_name', text='Name')
        bookings_treeview.heading('price', text='Price')
        bookings_treeview.heading('seats', text='Seats')
        bookings_treeview.heading('date', text='Date')
        bookings_treeview.heading('time', text='Time')

        bookings_treeview.column('show_name', width=100, anchor=tk.W)
        bookings_treeview.column('price', width=100, anchor=tk.W)
        bookings_treeview.column('seats', width=100, anchor=tk.W)
        bookings_treeview.column('date', width=100, anchor=tk.W)
        bookings_treeview.column('time', width=100, anchor=tk.W)


        for one_booking in self.USER_BOOKINGS:
            name = one_booking[0]
            date, time = self.AVAILABLE_SHOWS[name][0], self.AVAILABLE_SHOWS[name][1]
            price, seats = one_booking[1], ", ".join(one_booking[2])
            temp = [name, date, time, price, seats]
            # SELECTED_SHOWS[key] = float(value[-1][1:])
            print(name)
            bookings_treeview.insert('', tk.END, values=temp)
        bookings_treeview.grid(row=1, column=0)

        # Buttons
        next_btn = ttk.Button(
            self, text="Delete", command=lambda: self.cancel_booking(bookings_treeview))
        next_btn.grid(row=2, column=1)
        go_back_btn = ttk.Button(
            self, text="Go back", command=lambda: controller.show_frame("Dashboard"))
        go_back_btn.grid(row=3, column=1)

    def cancel_booking(self, bookings_treeview):
        seats = self.controller.get_seats()
        order_obj = self.selected_item(bookings_treeview)
        order = order_obj["values"]
        print(order)
        order_seats = order[4].split(", ")
        for seat in seats:
            if seat in order_seats:
                seats[seat] = "available"
        for user_booking in range(len(self.USER_BOOKINGS)):
            info = (self.USER_BOOKINGS[user_booking])[:2]
            print(info)
            info.append(order_seats)
            print(user_booking, info)
            if self.USER_BOOKINGS[user_booking] == info:
                print("thing deleted???")
                del self.USER_BOOKINGS[user_booking]
                print(bookings_treeview)
        self.controller.show_frame("Dashboard")


    def selected_item(self, bookings_treeview):
        curItem = bookings_treeview.focus()
        return bookings_treeview.item(curItem)
    