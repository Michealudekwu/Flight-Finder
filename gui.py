from tkinter import *
from tkinter import messagebox
import json
from PIL import Image, ImageTk
from city_iata_find import FlightSearch
from flight_data import FlightData

#=================================UI==========================================================
class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flight Pricer")
        self.window.config(padx=30, pady=30, bg="#f0f4f7")
        self.subscribe_var = IntVar()
        # === Load and Resize Image ===
        img = Image.open("plane_png/plane2.png")
        resized_img = img.resize((120, 120))
        plane_png = ImageTk.PhotoImage(resized_img)

        # === Header ===
        header = Label(self.window, text="Flight Pricer", font=("Arial", 20, "bold"), bg="#f0f4f7")
        header.grid(column=0, row=0, columnspan=4, pady=(0, 10))

        self.canvas = Canvas(self.window, width=120, height=120, bg="#f0f4f7", highlightthickness=0)
        self.canvas.create_image(60, 60, image=plane_png)
        self.canvas.grid(column=0, row=1, columnspan=4, pady=(0, 20))

        # === Personal Info ===
        first_name = Label(text="First Name:", bg="#f0f4f7", font=("Arial", 10))
        first_name.grid(column=0, row=2, sticky="e", padx=5, pady=5)
        self.first_gap = Entry(width=25)
        self.first_gap.grid(column=1, row=2, padx=5, pady=5)

        second_name = Label(text="Surname:", bg="#f0f4f7", font=("Arial", 10))
        second_name.grid(column=2, row=2, sticky="e", padx=5, pady=5)
        self.second_gap = Entry(width=25)
        self.second_gap.grid(column=3, row=2, padx=5, pady=5)

        phone_label = Label(text="Phone:", bg="#f0f4f7", font=("Arial", 10))
        phone_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)
        self.phone_gap = Entry(width=25)
        self.phone_gap.grid(column=1, row=3, padx=5, pady=5)

        # === Flight Info ===
        from_label = Label(text="City:", bg="#f0f4f7", font=("Arial", 10))
        from_label.grid(column=0, row=4, sticky="e", padx=5, pady=5)
        self.from_gap = Entry(width=25)
        self.from_gap.grid(column=1, row=4, padx=5, pady=5)

        to_label = Label(text="Arrival:", bg="#f0f4f7", font=("Arial", 10))
        to_label.grid(column=2, row=4, sticky="e", padx=5, pady=5)
        self.to_gap = Entry(width=25)
        self.to_gap.grid(column=3, row=4, padx=5, pady=5)

        date1_label = Label(text="From:", bg="#f0f4f7", font=("Arial", 10))
        date1_label.grid(column=0, row=5, sticky="e", padx=5, pady=5)
        self.date1_gap = Entry(width=25)
        self.date1_gap.grid(column=1, row=5, padx=5, pady=5)

        date2_label = Label(text="To:", bg="#f0f4f7", font=("Arial", 10))
        date2_label.grid(column=2, row=5, sticky="e", padx=5, pady=5)
        self.date2_gap = Entry(width=25)
        self.date2_gap.grid(column=3, row=5, padx=5, pady=5)

        # === Submit Button ===
        submit_btn = Button(self.window, text="Search Flights", bg="#007acc", fg="white", command=self.get_info,
                            font=("Arial", 12, "bold"), padx=10, pady=5)
        submit_btn.grid(column=0, row=7, columnspan=2, pady=20)

        self.details = Button(self.window, text="Flight Details", fg="black", command=self.read_flight,
                            font=("Arial", 12, "bold"), padx=10, pady=5, state="disabled")
        self.details.grid(column=2, row=7, columnspan=2, pady=20)

        self.subscribe_check = Checkbutton(self.window, text="Nonstop?", variable=self.subscribe_var)
        self.subscribe_check.grid(column=0, row=6, columnspan=4, pady=20)


        self.window.mainloop()


    def clear(self):
        self.first_gap.delete(0, END)
        self.second_gap.delete(0, END)
        self.date1_gap.delete(0, END)
        self.date2_gap.delete(0, END)
        self.phone_gap.delete(0, END)
        self.from_gap.delete(0, END)
        self.to_gap.delete(0, END)


    def get_info(self):
        first_name = self.first_gap.get()
        second_name = self.second_gap.get()
        phone = self.phone_gap.get()
        date1 = self.date1_gap.get()
        date2 = self.date2_gap.get()
        from_city = self.from_gap.get()
        to_city = self.to_gap.get()

        fills = 0

        info = [first_name,second_name, phone, date2, date1, from_city, to_city]

        for infos in info:
            if len(infos) > 0:
                fills+=1
        if fills != len(info):
            messagebox.showerror(title="INPUT ERROR", message="Please fill all empty gaps")

        else:
            nonstop = "false"
            iata = FlightSearch([from_city, to_city])
            codes = iata.iata
            if self.subscribe_var.get():
                nonstop = "true"

            new_data = {
                second_name: {
                    "first Name": first_name,
                    "phone": phone,
                    "going_date": date1,
                    "arrival_date": date2,
                    "from_city": from_city,
                    "to_city": to_city,
                    "from_iata": codes[0],
                    "to_iata": codes[1],
                    "nonstop": nonstop
                }
            }

            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
            token = iata.get_token
            flight = FlightData(token, second_name)
            self.details.config(state="normal", font=("Arial", 12, "bold"), bg="#007acc")

            self.clear()

    def read_flight(self):
        with open("flight_data.json", "r") as flight:
            flight_data = json.load(flight)
            price = flight_data["lowest_price"]
            departure_code = flight_data["departure_airport_code"]
            arrival_code = flight_data["arrival_airport_code"]
            outbound_date = flight_data["outbound_date"]
            inbound_date = flight_data["inbound_date"]

        messagebox.showinfo(title="FLIGHT DETAILS",
                            message=f"Flight Details...\n "
                                    f"Price = {price}\n "
                                    f"Departure = {departure_code}\n"
                                    f"Arrival = {arrival_code}\n"
                                    f"Leave At = {outbound_date}\n"
                                    f"Lands At = {inbound_date}"
                            )



