"""
Description: Main client program to test the library system functionalities.
Author: Enzo Kneipp
"""

from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser
from borrower_status.borrower_status import BorrowerStatus
from genre.genre import Genre

def main():
    # Test LibraryItem class with updated details
    try:
        item = LibraryItem("The Pragmatic Programmer", "Andy Hunt", Genre.NON_FICTION, 101, False)
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Genre: {item.genre.name}")
        print(f"Item ID: {item.item_id}")
        print(f"Is Borrowed: {item.is_borrowed}")
    except Exception as e:
        print(e)

    # Test LibraryUser class with updated name and email
    try:
        user = LibraryUser(101, "Enzo Kneipp", "kneippenzo@gmail.com", BorrowerStatus.ACTIVE)
        print(f"User ID: {user.user_id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Borrower Status: {user.borrower_status.name}")
        print(user.borrow_item())
        print(user.return_item())
    except Exception as e:
        print(e)

    # Test with invalid inputs
    try:
        invalid_user = LibraryUser(99, "", "invalidemail", BorrowerStatus.ACTIVE)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
