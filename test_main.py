
import unittest
from phonebook import *


class PhoneBookTest(unittest.TestCase):

    def test_create_phonebook(self):
        pbook = Phonebook()

    def test_lookup_entry_by_name(self):
        pbook = Phonebook()
        pbook.add('bob', '12345')
        self.assertEqual('12345', pbook.lookup('bob'))

    def test_missing_entry_raises_keyerror(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")
