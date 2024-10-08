# password_generator.py
from random import choice, randint, shuffle
import pyperclip

class PasswordGenerator:
    @staticmethod
    def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pass_letter = [choice(letters) for _ in range(randint(8, 10))]
        pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]
        pass_number = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = pass_letter + pass_number + pass_symbol
        shuffle(password_list)

        password = "".join(password_list)
        pyperclip.copy(password)
        return password
