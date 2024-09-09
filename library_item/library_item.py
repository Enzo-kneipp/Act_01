"""
Description: This file is what defines the LibraryItem class, which represents an item in the libraryclass on its own.
Author: Enzo Kneipp
date:sep/06
"""

from genre.genre import Genre

class LibraryItem:
    """
    Represents an item in the library.

    Attributes:
        title (str): The title of the library item.
        author (str): The author of the library item.
        genre (Genre): The genre of the library item.
        item_id (int): The unique ID of the library item.
        is_borrowed (bool): Whether the item is currently borrowed or not.
    """

    def __init__(self, title, author, genre, item_id, is_borrowed):
        """
        Initializes a LibraryItem object with the given title, author, genre, item ID, and borrowed status.

        Args:
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The genre of the library item.
            item_id (int): The unique ID of the library item.
            is_borrowed (bool): The borrowed status of the library item.

        Raises:
            ValueError: If the title, author, or genre are invalid, or if the item_id is less than 100.
        """
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be blank.")
        if len(author.strip()) == 0:
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        
    """ self.__title = title.strip()
        self.__author = author.strip()
        self.__genre = genre
        self.__item_id = item_id
        self.__is_borrowed = is_borrowed
        """
    @property
    def title(self):
        """Returns the title of the library item."""
        return self.__title

    @property
    def author(self):
        """Returns the author of the library item."""
        return self.__author

    @property
    def genre(self):
        """Returns the genre of the library item."""
        return self.__genre

    @property
    def item_id(self):
        """Returns the id of the library item."""
        return self.__item_id

    @property
    def is_borrowed(self):
        """Returns whether the library item is borrowed."""
        return self.__is_borrowed