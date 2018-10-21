
# unittest is python's base unit testing module
# to run 'test cases', run python -m unittest in terminal in the directory of the test file/suite
# BE SURE THE FILE AND ALL FUNCTIONS START WITH TEST OR IT WILL NOT FIND THE TEST CASE
import unittest
from phonebook import *


class PhoneBookTest(unittest.TestCase):  # derives from unittest as stated above

    # setup and teardown are known as test fixtures
    def setUp(self):  # will run before every test method
        self.phonebook = Phonebook()

    def tearDown(self):  # will run for cleanup after each test
        pass  # here we don't need to 'tearDown' anything, so its just pass
        # this will still run EVEN if an exception is thrown

    def test_create_phonebook(self):
        pass

    def test_lookup_entry_by_name(self):
        self.phonebook.add('bob', '12345')
        self.assertEqual('12345', self.phonebook.lookup('bob'))  # test will pass if the parameters are equal
        # or 'Assert' that these two values (expected, actual) are equal

    def test_missing_entry_raises_keyerror(self):
        with self.assertRaises(KeyError):  # assert that this method raises an exception
            self.phonebook.lookup("missing")

    @unittest.skip("Work in progress")  # tells python test runner to ignore this function as it is "work in progress"
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())  # assert that the parameters are true
