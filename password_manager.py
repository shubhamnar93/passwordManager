# password_manager.py
import json

class PasswordManager:
    @staticmethod
    def save_password(website, email, password):
        new_data = {
            website: {
                'Email': email,
                'Password': password
            }
        }

        try:
            with open("password_data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open("password_data.json", "w") as f:
            json.dump(data, f, indent=4)
