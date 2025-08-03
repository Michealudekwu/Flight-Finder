# ✈️ Flight Pricer

A desktop GUI app that helps you search and compare flight prices between cities using the Amadeus Flight Offers API.

![Flight Pricer UI](plane_png/plane2.png)

---

## 🚀 Features

- 🔍 Search flights between two cities
- 📅 Select travel dates with a calendar widget
- 🔄 Option to search nonstop or all available flights
- 💸 Displays the cheapest flight price
- 🧾 Saves flight info for quick reference
- 🎨 Simple and intuitive Tkinter GUI

---

## 🛠️ Tech Stack

- **Python 3.11+**
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — for GUI
- [tkcalendar](https://pypi.org/project/tkcalendar/) — for date selection
- [Pillow](https://pypi.org/project/Pillow/) — for image handling
- [Requests](https://pypi.org/project/requests/) — for API communication
- [python-dotenv](https://pypi.org/project/python-dotenv/) — to manage API keys
- [Amadeus API](https://developers.amadeus.com/) — flight data

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/flight-pricer.git
cd flight-pricer
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
API_KEY=your_amadeus_api_key
API_SECRET=your_amadeus_api_secret
```

▶️ How to Run
bash
python main.py

📁 Project Structure
flight_pricer/
│
├── gui.py              # Tkinter GUI logic
├── flight_data.py      # Flight price fetching logic
├── city_iata_find.py   # IATA code lookup using Amadeus
├── data_manager.py     # Handles reading user inputs from file
├── main.py             # Entry point to launch the app
├── data.json           # Stores user flight search info
├── flight_data.json    # Stores cheapest flight found
├── .env                # API credentials (not included in repo)
├── requirements.txt    # Project dependencies
└── plane_png/          # Folder for the airplane image


---

### 📌 Tips

- Replace `your_amadeus_api_key` with your actual API credentials in your `.env` (never commit this file).
- Replace `your-username` and `[Your Name]` with your GitHub info.
- Add screenshots for better appeal.


