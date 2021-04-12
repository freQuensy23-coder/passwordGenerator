from hashlib import sha224


class Password_generator:
    def __init__(self):
        """Class that generates password by user name colour url, and secret pass"""
        self.alphabet = "abcdefgefghigklmnopqrstuvwxyz"
        self.alphabet += self.alphabet.upper() + "0123456789"
        self.password_len = 15
        self.available_colors = {
            "red": 0,
            "green": 1,
            "blue": 2,
            "yellow": 3,
            "black": 4,
            "pink": 5
        }

    def generate(self, user_name: str, secret_pass: str, color: str, url: str):
        # TODO Replasce smth like http:// and www to make url unified
        return sha224(bytes(user_name + secret_pass + color + url, encoding="utf8")).hexdigest()[:self.password_len]
