from unittest import TestCase
from Core import Password_generator


class Tester(TestCase):
    def setUp(self) -> None:
        self.pass_gen = Password_generator()

    def test_generate_password(self):
        self.assertEqual(type(self.pass_gen.generate("Alex", "2131332131311", "green", "https://www.vk.com")), str)
        self.assertEqual(len(self.pass_gen.generate("Alex", "2131332131311", "green", "https://www.vk.com")), self.pass_gen.password_len)