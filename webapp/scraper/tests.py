from django.test import TestCase
from django.urls import reverse
from .models import Entry


# Utilities
def generate_entries(to_dict=False, size=3):
    """Utility for faking entries."""
    entries = []
    for i in range(size):
        entry = Entry(i, f"Entry #{i}", i**2, i**3)
        entries.append(entry.to_dict() if to_dict else entry)
    return entries


# # Create your tests here.
# class SessionStorageTest(TestCase):
#     """Class for testing session storage."""

#     def setUp(self):
#         """Clear session storage for every test case."""
#         self.client.session.clear()

#     def test_session_storage_for_entries(self):
#         """Test session storage to save and retrieve entries."""
#         session = self.client.session
#         session["entries"] = []
#         session.save()
#         self.assertEqual(len(session["entries"]), 0)
#         session["entries"] = generate_entries(True)
#         session.save()
#         self.assertEqual(len(session["entries"]), 3)


# class ViewTest(TestCase):
#     """Class for testing the main view of the app."""

#     def setUp(self):
#         """Clear session storage for every test case."""
#         self.client.session.clear()

#     def test_view_with_session_data(self):
#         session = self.client.session
#         self.assertEqual(session.get("entries"), None)
#         response = self.client.get(reverse("entries"))
#         self.assertEqual(len(session.get("entries", [])), 30)


class EntryTest(TestCase):
    """Class for testing Entry class."""

    def test_entry_initialization(self):
        """Test entry object initialization."""
        entry = Entry(1, "Title", 2, 3)
        self.assertEqual(entry.number, 1)
        self.assertEqual(entry.title, "Title")
        self.assertEqual(entry.points, 2)
        self.assertEqual(entry.comments, 3)

    def test_count_words(self):
        """Test count words."""
        entry = Entry(1, "Title with four words", 2, 3)
        self.assertEqual(entry.words, 4)
        entry = Entry(4, "This is - a self-explained example", 5, 6)
        self.assertEqual(entry.words, 5)
        entry = Entry(1, "- -Title- with ? 3", 2, 3)
        self.assertEqual(entry.words, 3)
