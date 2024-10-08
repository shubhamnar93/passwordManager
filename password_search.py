# password_searcher.py
import json
from tkinter import messagebox

class PasswordSearcher:
    @staticmethod
    def search_password(website):
        try:
            with open("password_data.json", "r") as f:
                data = json.load(f)
            return data[website]
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found")
        except KeyError:
            messagebox.showwarning(title="Error", message="No data found")

