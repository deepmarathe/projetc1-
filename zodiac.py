import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ZodiacSignFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zodiac Sign Finder")
        self.geometry("500x300")
        self.configure(bg="#f9f7f7")
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self, text="Zodiac Sign Finder", font=("Helvetica", 24, "bold"), fg="#2c3e50", bg="#f9f7f7")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.label_name = tk.Label(self, text="Name:", font=("Helvetica", 14), fg="#2c3e50", bg="#f9f7f7")
        self.label_name.grid(row=1, column=0, sticky="e", padx=(20, 10), pady=(10, 5))
        self.entry_name = tk.Entry(self, font=("Helvetica", 14), width=30, bg="#ffffff", relief=tk.FLAT, highlightbackground="#bdc3c7", highlightcolor="#bdc3c7", highlightthickness=2)
        self.entry_name.grid(row=1, column=1, padx=(0, 20), pady=(10, 5))

        self.label_dob = tk.Label(self, text="Date of Birth (YYYY-MM-DD):", font=("Helvetica", 14), fg="#2c3e50", bg="#f9f7f7")
        self.label_dob.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(5, 5))
        self.entry_dob = tk.Entry(self, font=("Helvetica", 14), width=30, bg="#ffffff", relief=tk.FLAT, highlightbackground="#bdc3c7", highlightcolor="#bdc3c7", highlightthickness=2)
        self.entry_dob.grid(row=2, column=1, padx=(0, 20), pady=(5, 5))

        self.button_submit = tk.Button(self, text="Find Zodiac Sign", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#27ae60", activebackground="#2ecc71", relief=tk.FLAT, command=self.get_zodiac_sign)
        self.button_submit.grid(row=3, column=0, columnspan=2, pady=(20, 10))

        self.button_clear = tk.Button(self, text="Clear Fields", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#e74c3c", activebackground="#c0392b", relief=tk.FLAT, command=self.clear_fields)
        self.button_clear.grid(row=4, column=0, columnspan=2)

    def calculate_zodiac_sign(self, day, month):
        zodiac_signs = [
            ("Capricorn", (1, 20), (2, 18)),
            ("Aquarius", (2, 19), (3, 20)),
            ("Pisces", (3, 21), (4, 19)),
            ("Aries", (4, 20), (5, 20)),
            ("Taurus", (5, 21), (6, 20)),
            ("Gemini", (6, 21), (7, 22)),
            ("Cancer", (7, 23), (8, 22)),
            ("Leo", (8, 23), (9, 22)),
            ("Virgo", (9, 23), (10, 22)),
            ("Libra", (10, 23), (11, 21)),
            ("Scorpio", (11, 22), (12, 21)),
            ("Sagittarius", (12, 22), (12, 31))
        ]
        for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return sign
        return None

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_dob.delete(0, tk.END)

    def get_zodiac_sign(self):
        name = self.entry_name.get().strip()
        dob = self.entry_dob.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not dob:
            messagebox.showerror("Error", "Please enter your date of birth.")
            return
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d")
            zodiac_sign = self.calculate_zodiac_sign(dob_date.day, dob_date.month)
            if zodiac_sign:
                messagebox.showinfo("Zodiac Sign", f"Hello {name}, your zodiac sign is {zodiac_sign}.")
            else:
                messagebox.showwarning("Invalid Date", "Please enter a valid date of birth.")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date of birth in the format YYYY-MM-DD.")

if __name__ == "__main__":
    app = ZodiacSignFinderApp()
    app.mainloop()
