"""
Description: This file defines the LibraryUser class, which represents a user of the library system.
Author: Enzo Kneipp
Date:sep/06
"""

from email_validator import validate_email, EmailNotValidError
from borrower_status import BorrowerStatus

class LibraryUser:
    """
    Represents a user of the library.

    Attributes:
        user_id (int): The unique user id value of the library user.
        name (str): The name of the library user.
        email (str): The email address of the library user.
        borrower_status (BorrowerStatus): The current status of the library user.
    """

    def __init__(self, user_id: int, name: str, email: str, borrower_status: BorrowerStatus):
        """
        Initializes a new instance of the LibraryUser class.

        Args:
            user_id (int): The unique user id value of the library user.
            name (str): The name of the library user.
            email (str): The email address of the library user.
            borrower_status (BorrowerStatus): The current status of the library user.

        Raises:
            ValueError: If the user_id is not an integer or less than 100, name is blank, email is invalid, or borrower_status is invalid.
        """
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        if user_id <= 99:
            raise ValueError("Invalid User Id.")
        self.__user_id = user_id

        if len(name.strip()) == 0:
            raise ValueError("Name cannot be blank.")
        self.__name = name

        try:
            validate_email(email)
        except EmailNotValidError:
            raise ValueError("Invalid email address.")
        self.__email = email

        if not isinstance(borrower_status, BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")
        self.__borrower_status = borrower_status

    @property
    def user_id(self) -> int:
        """
        Gets the user id of the library user.

        Returns:
            int: The user id of the library user.
        """
        return self.__user_id

    @property
    def name(self) -> str:
        """
        Gets the name of the library user.

        Returns:
            str: The name of the library user.
        """
        return self.__name

    @property
    def email(self) -> str:
        """
        Gets the email address of the library user.

        Returns:
            str: The email address of the library user.
        """
        return self.__email

    @property
    def borrower_status(self) -> BorrowerStatus:
        """
        Gets the borrower status of the library user.

        Returns:
            BorrowerStatus: The current status of the library user.
        """
        return self.__borrower_status

    def borrow_item(self) -> str:
        """
        Determines if the user can borrow an item.

        Returns:
            str: A message indicating whether the user can borrow an item.

        Raises:
            Exception: If the user cannot borrow an item due to their status.
        """
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception(f"{self.__name} cannot borrow an item due to their {self.__borrower_status.name} status.")
        return f"{self.__name} is eligible to borrow the item."

    def return_item(self) -> str:
        """
        Processes the return of an item by the user.

        Returns:
            str: A message indicating the result of the return process.
        """
        if self.__borrower_status == BorrowerStatus.DELINQUENT:
            self.__borrower_status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self.__name} has returned the item, status now changed to: {self.__borrower_status.name}."
        return "Item successfully returned."
