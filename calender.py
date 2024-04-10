import tkinter as tk
from tkinter import ttk
from datetime import date, timedelta

# Define English to Nepali translations
translations = {
    "Day": "दिन",
    "Week": "सप्ताह",
    "Month": "महिना",
    "Year": "वर्ष",
    "Prev": "पूर्व",
    "Next": "अघि",
    "Sunday": "आइतबार",
    "Monday": "सोमबार",
    "Tuesday": "मंगलबार",
    "Wednesday": "बुधबार",
    "Thursday": "बिहिबार",
    "Friday": "शुक्रबार",
    "Saturday": "शनिबार",
    "January": "जनवरी",
    "February": "फेब्रुअरी",
    "March": "मार्च",
    "April": "अप्रिल",
    "May": "मे",
    "June": "जुन",
    "July": "जुलाई",
    "August": "अगस्ट",
    "September": "सेप्टेम्बर",
    "October": "अक्टोबर",
    "November": "नोभेम्बर",
    "December": "डिसेम्बर",
    "Baishakh": "बैशाख"
}

# Define months and their lengths in Nepali calendar
nepali_months = {
    "Baishakh": 31,
    "Jestha": 31,
    "Asar": 30,
    "Shrawan": 31,
    "Bhadra": 31,
    "Ashoj": 30,
    "Kartik": 29,
    "Mangsir": 29,
    "Poush": 29,
    "Magh": 29,
    "Falgun": 29,
    "Chaitra": 30
}

class NepaliCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("नेपाली क्यालेन्डर एप")
        self.selected_date = date.today()

        self.calendar_frame = ttk.Frame(root)
        self.calendar_frame.pack(padx=10, pady=10)

        self.month_label = ttk.Label(self.calendar_frame, text="Month:")
        self.month_label.grid(row=0, column=0, padx=5, pady=5)
        self.month_name_label = ttk.Label(self.calendar_frame, text="")
        self.month_name_label.grid(row=0, column=1, padx=5, pady=5)

        self.week_label = ttk.Label(self.calendar_frame, text="Week:")
        self.week_label.grid(row=1, column=0, padx=5, pady=5)
        self.week_number_label = ttk.Label(self.calendar_frame, text="")
        self.week_number_label.grid(row=1, column=1, padx=5, pady=5)

        self.day_label = ttk.Label(self.calendar_frame, text="Day:")
        self.day_label.grid(row=2, column=0, padx=5, pady=5)
        self.day_number_label = ttk.Label(self.calendar_frame, text="")
        self.day_number_label.grid(row=2, column=1, padx=5, pady=5)

        self.calendar_label = ttk.Label(self.calendar_frame, text="")
        self.calendar_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        # Create buttons with Nepali text
        self.day_button = ttk.Button(self.button_frame, text=translations["Day"], command=self.view_day)
        self.day_button.grid(row=0, column=0, padx=5)
        self.week_button = ttk.Button(self.button_frame, text=translations["Week"], command=self.view_week)
        self.week_button.grid(row=0, column=1, padx=5)
        self.month_button = ttk.Button(self.button_frame, text=translations["Month"], command=self.view_month)
        self.month_button.grid(row=0, column=2, padx=5)
        self.year_button = ttk.Button(self.button_frame, text=translations["Year"], command=self.view_year)
        self.year_button.grid(row=0, column=3, padx=5)

        self.prev_button = ttk.Button(self.button_frame, text=translations["Prev"], command=self.prev_period)
        self.prev_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="ew")
        self.next_button = ttk.Button(self.button_frame, text=translations["Next"], command=self.next_period)
        self.next_button.grid(row=1, column=2, padx=5, pady=5, columnspan=2, sticky="ew")

        self.update_calendar()

    def update_calendar(self):
        self.month_name_label.config(text=self.selected_date.strftime("%B"))
        self.week_number_label.config(text=str(self.selected_date.isocalendar()[1]))
        self.day_number_label.config(text=str(self.selected_date.day))
        self.calendar_label.config(text=self.get_calendar_text())

    def get_calendar_text(self):
        return f"Selected Date: {self.selected_date}"

    def view_day(self):
        self.calendar_label.config(text=f"Selected Date: {self.selected_date}")

    def view_week(self):
        start_date = self.selected_date - timedelta(days=self.selected_date.weekday())
        end_date = start_date + timedelta(days=6)
        week_text = " ".join([f"{translations[day.strftime('%A')]}: {day}" for day in self.get_week_days(start_date)])
        self.calendar_label.config(text=f"Selected Week: {week_text}")

    def view_month(self):
        month_text = "\n".join([f"{translations[self.selected_date.strftime('%B')]}: {day}" for day in self.get_month_days()])
        self.calendar_label.config(text=f"Selected Month: \n{month_text}")

    def view_year(self):
        start_date = date(self.selected_date.year, 1, 1)
        end_date = date(self.selected_date.year, 12, 31)
        self.calendar_label.config(text=f"Selected Year: {self.selected_date.year}")

    def prev_period(self):
        if self.week_button["state"] == "normal":
            self.selected_date -= timedelta(weeks=1)
            self.view_week()
        elif self.month_button["state"] == "normal":
            self.selected_date = self.selected_date.replace(day=1) - timedelta(days=1)
            self.view_month()
        elif self.year_button["state"] == "normal":
            self.selected_date = date(self.selected_date.year - 1, 1, 1)
            self.view_year()

    def next_period(self):
        if self.week_button["state"] == "normal":
            self.selected_date += timedelta(weeks=1)
            self.view_week()
        elif self.month_button["state"] == "normal":
            self.selected_date = date(self.selected_date.year, self.selected_date.month + 1, 1)
            self.view_month()
        elif self.year_button["state"] == "normal":
            self.selected_date = date(self.selected_date.year + 1, 1, 1)
            self.view_year()

    def get_week_days(self, start_date):
        return [start_date + timedelta(days=i) for i in range(7)]

    def get_month_days(self):
        days_in_month = nepali_months[self.selected_date.strftime("%B")]
        first_day_of_month = date(self.selected_date.year, self.selected_date.month, 1)
        return [first_day_of_month + timedelta(days=i) for i in range(days_in_month)]

def main():
    root = tk.Tk()
    app = NepaliCalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
