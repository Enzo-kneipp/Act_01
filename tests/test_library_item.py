
"""
Description: Contains unit tests for the LibraryItem class.
Author: Enzo Kneipp
"""

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre

class TestLibraryItem(unittest.TestCase):
    def test_init_valid(self):
        """Tests initialization with valid arguments."""
        item = LibraryItem("Title", "Author", Genre.FICTION, 1, False)
        self.assertEqual(item.title, "Title")
        self.assertEqual(item.author, "Author")
        self.assertEqual(item.genre, Genre.FICTION)
        self.assertEqual(item.item_id, 1)
        self.assertFalse(item.is_borrowed)

    def test_init_blank_title(self):
        """Tests initialization with a blank title."""
        with self.assertRaises(ValueError):
            LibraryItem("", "Author", Genre.FICTION, 1, False)

    def test_init_blank_author(self):
        """Tests initialization with a blank author."""
        with self.assertRaises(ValueError):
            LibraryItem("Title", "", Genre.FICTION, 1, False)

    def test_init_invalid_genre(self):
        """Tests initialization with an invalid genre."""
        with self.assertRaises(ValueError):
            LibraryItem("Title", "Author", "InvalidGenre", 1, False)

    def test_init_invalid_item_id(self):
        """Tests initialization with an invalid item_id."""
        with self.assertRaises(ValueError):
            LibraryItem("Title", "Author", Genre.FICTION, "InvalidId", False)

    def test_init_invalid_is_borrowed(self):
        """Tests initialization with an invalid is_borrowed."""
        with self.assertRaises(ValueError):
            LibraryItem("Title", "Author", Genre.FICTION, 1, "InvalidBool")
