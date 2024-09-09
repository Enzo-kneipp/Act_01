"""
Description: This file defines the LibraryUser class, which represents a user of the library system.
Author: Enzo Kneipp
Date:sep/06
"""

from borrower_status.borrower_status import BorrowerStatus

class LibraryUser:
    """
    Represents a user of the library system.

    Attributes:
        user_id (int): The unique user ID.
        name (str): The name of the user.
        email (str): The email address of the user.
        borrower_status (BorrowerStatus): The status of the borrower (ACTIVE, DELINQUENT, etc.).
    """

    def __init__(self, user_id: int, name: str, email: str, borrower_status: BorrowerStatus):
        """
        Initializes a LibraryUser object with the given user ID, name, email, and borrower status.

        Args:
            user_id (int): The unique user ID.
            name (str): The name of the user.
            email (str): The email address of the user.
            borrower_status (BorrowerStatus): The current status of the borrower.

        Raises:
            ValueError: If user_id is not an integer, is less than 100, if name is blank, if the email is invalid,
                        or if borrower_status is not a valid BorrowerStatus.
        """
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        if user_id <= 99:
            raise ValueError("Invalid User Id.")
        if not name.strip():
            raise ValueError("Name cannot be blank.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")
        if not isinstance(borrower_status, BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")

        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__borrower_status = borrower_status

    @property
    def user_id(self):
        """Returns the user's ID."""
        return self.__user_id

    @property
    def name(self):
        """Returns the user's name."""
        return self.__name

    @property
    def email(self):
        """Returns the user's email address."""
        return self.__email

    @property
    def borrower_status(self):
        """Returns the user's borrower status."""
        return self.__borrower_status

    def borrow_item(self) -> str:
        """
        Checks if the user is eligible to borrow an item based on their borrower status.

        Returns:
            str: A message indicating the borrowing eligibility.

        Raises:
            Exception: If the user's borrower status is DELINQUENT.
        """
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception(f"{self.__name} cannot borrow an item due to their {self.__borrower_status.name} status.")
        return f"{self.__name} is eligible to borrow the item."

    def return_item(self) -> str:
        """
        Handles the return of an item and updates the user's borrower status if necessary.

        Returns:
            str: A message indicating the return status.
        """
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            self.__borrower_status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self.__name} has returned the item, status now changed to: {self.__borrower_status.name}."
        return "Item successfully returned."
