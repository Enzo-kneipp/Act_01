"""
Description: Unit tests for the LibraryUser class.
Author: {Enzo Kneipp}
Date: {sep/08}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

import unittest
from email_validator import EmailNotValidError
from library_user import LibraryUser
from borrower_status import BorrowerStatus

class TestLibraryUser(unittest.TestCase):

    def test_init_invalid_user_id_raises_exception(self):
        # Arrange
        user_id = "one"  # Invalid user_id
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertEqual(str(context.exception), "User Id must be numeric.")

    def test_init_user_id_less_than_100_raises_exception(self):
        # Arrange
        user_id = 99  # Invalid user_id
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertEqual(str(context.exception), "Invalid User Id.")

    def test_init_blank_name_raises_exception(self):
        # Arrange
        user_id = 100
        name = ""
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertEqual(str(context.exception), "Name cannot be blank.")

    def test_init_invalid_email_raises_exception(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "invalid-email"
        borrower_status = BorrowerStatus.ACTIVE

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertEqual(str(context.exception), "Invalid email address.")

    def test_init_invalid_borrower_status_raises_exception(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = "Invalid Status"  # Invalid borrower_status

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertEqual(str(context.exception), "Invalid Borrower Status.")

    def test_init_valid_inputs(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE

        # Act
        user = LibraryUser(user_id, name, email, borrower_status)

        # Assert
        self.assertEqual(user.user_id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.borrower_status, borrower_status)

    def test_borrow_item_delinqent_status_raises_exception(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.DELINQUENT
        user = LibraryUser(user_id, name, email, borrower_status)

        # Act & Assert
        with self.assertRaises(Exception) as context:
            user.borrow_item()
        self.assertEqual(str(context.exception), f"{name} cannot borrow an item due to their {borrower_status.name} status.")

    def test_borrow_item_active_status(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE
        user = LibraryUser(user_id, name, email, borrower_status)

        # Act
        result = user.borrow_item()

        # Assert
        self.assertEqual(result, f"{name} is eligible to borrow the item.")

    def test_return_item_delinqent_status(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.DELINQUENT
        user = LibraryUser(user_id, name, email, borrower_status)

        # Act
        result = user.return_item()

        # Assert
        self.assertEqual(result, f"Item successfully returned. {name} has returned the item, status now changed to: {BorrowerStatus.ACTIVE.name}.")
        self.assertEqual(user.borrower_status, BorrowerStatus.ACTIVE)

    def test_return_item_active_status(self):
        # Arrange
        user_id = 100
        name = "Enzo Kneipp"
        email = "Kneippenzo@gmail.com"
        borrower_status = BorrowerStatus.ACTIVE
        user = LibraryUser(user_id, name, email, borrower_status)

        # Act
        result = user.return_item()

        # Assert
        self.assertEqual(result, "Item successfully returned.")

if __name__ == '__main__':
    unittest.main()