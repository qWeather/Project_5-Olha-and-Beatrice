import tkinter as tk
from tkinter import ttk
from Credentials import Login, Register
from Dashboard import Dashboard
<<<<<<< Updated upstream
from Bookings import Bookings, Seats, Summary
from Register import Register
=======
from Bookings import Bookings, Seats
from UserBookings import UserBookings
>>>>>>> Stashed changes

LARGEFONT = ("Verdana", 15)
SMALLFONT = ("Veredana", 10)

CREDENTIALS = {"beatrice": ["waterfall", "Beatrice Antoniu", "07567890102", "m.beea@yahoo.com"]}
BOOKINGS = {}
AVAILABLE_SHOWS = {
    "Stewart Lee's Comedy Vehicle": ["20/12/2022", "8PM", "150", "Sketches by stand-up comedian Stewart Lee and his friends in Newington Green", "£13.5"],
    "The Mary Whitehouse Experience": ["30/10/2022", "9PM", "200", "Topical sketch by David Baddiel, Rob Newman, Steve Punt, and Hugh Dennis.", "£15"]
}
AVAILABLE_SEATS = {
    "14B": "occupied",
    "12C": "available",
    "09A": "available",
    "09E": "available",
    "03D": "occupied",
    "20C": "available",
    "10B": "available",
    "15F": "available",
    "16F": "occupied",
    "07G": "occupied",
    }

CURRENT_USER = ""

class Show_Booking_System(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Griffin Show - Booking System')
        self.geometry('800x600')
        self['bg']='#5d8a82'
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=50, pady=50)

        self.frames = {}

<<<<<<< Updated upstream
        for F in (Main, Login, Dashboard, Register, Bookings, Seats):
  
            frame = F(container, self)
=======
        for F in (Main, Login, Dashboard, Register, Bookings, Seats, UserBookings):
            frame = F(self.container, self)
>>>>>>> Stashed changes
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame("Main")

    def show_frame(self, page):
        if page == "Main":
            frame = self.frames[Main]
            frame.tkraise()
        elif page == "Login":
            frame = self.frames[Login]
            frame.tkraise()
        elif page == "Dashboard":
            frame = Dashboard(self.container, self)
            self.frames[Dashboard] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame = self.frames[Dashboard]
            frame.tkraise()
        elif page == "Register":
            frame = self.frames[Register]
            frame.tkraise()
        elif page == "Bookings":
            frame = Bookings(self.container, self)
            self.frames[Bookings] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame = self.frames[Bookings]
            frame.tkraise()
        elif page == "Seats":
            frame = self.frames[Seats]
            frame.tkraise()
        elif page == "Summary":
            frame = self.frames[Summary]
            frame.tkraise()
        elif page == "Seats":
            frame = Seats(self.container, self)
            self.frames[Seats] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame = self.frames[Seats]
            frame.tkraise()
        elif page == "UserBookings":
            frame = UserBookings(self.container, self)
            self.frames[UserBookings] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame = self.frames[UserBookings]
            frame.tkraise()
        else:
            print("Page doesn't exist!")
    
    def get_credentials(self):
        return CREDENTIALS

    def get_bookings(self):
        return BOOKINGS
    
    def get_shows(self):
        return AVAILABLE_SHOWS

    def get_seats(self):
        return AVAILABLE_SEATS

    def set_curr_user(self, username):
        global CURRENT_USER
        CURRENT_USER = username

    def get_curr_user(self):
        return CURRENT_USER


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        welcome_label = ttk.Label(self, text ="Welcome to the Griffin Show!", font = LARGEFONT)
        welcome_label.grid(column=0, row=0)
        notice_label = ttk.Label(self, text ="Are you already registered?", font = SMALLFONT)
        notice_label.grid(column=0, row=1)

        # Buttons
        login_btn = ttk.Button(self, text ="Login", command = lambda : controller.show_frame("Login"))
        login_btn.grid(row = 2, column = 0)
        register_btn = ttk.Button(self, text ="Register", command = lambda : controller.show_frame("Register"))
        register_btn.grid(row = 3, column = 0)

app = Show_Booking_System()
app.mainloop()


