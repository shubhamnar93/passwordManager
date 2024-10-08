This code help you to create, store, and manage your passwords loclly in your computer

1. `password_generator.py`: it return passwodr of random size having random number of random letter, symbol and number and copy it to clipboard

2. `password_manager.py`: it recieves website, email, password and put it in json file

3. `password_search.py`: it recive website and if website exist in json file it returns email and password of the website otherwise it return false

4. `main.py`: it setup entire GUI, it calls `generate_password` method from `PasswordGenerator` class and insert the password when `Generate Password` button is clicked, it calls `save_password` method from `PasswordManager` class and shows the error window if any of the feilds are empthy when `add` button is clicked, it calls `search_password` method from `PasswordSearcher` class and show message box when method do not return false when `search` button is clicked
