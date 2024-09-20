from django.test import TestCase
from django.urls import reverse
from .models import Entry, to_int
from .views import retrieve_entries
from urllib.parse import urlencode
from unittest.mock import patch
import requests

class TestSessionStorage(TestCase):
    """Class for testing session storage."""

    def setUp(self):
        """Runs before each test and clear session storage."""
        self.client.session.clear()

    def test_session_storage_for_entries(self):
        """It should save entries in session storage and then retrieve them."""
        session = self.client.session
        # Check entries is empty
        self.assertNotIn("entries", session)
        # Save entries
        session["entries"] = retrieve_entries(True)
        session.save()
        # Check entries were saved
        self.assertEqual(len(session["entries"]), 30)


class TestView(TestCase):
    """Class for testing the main view of the app."""

    def setUp(self):
        """Runs before each test and clear session storage."""
        self.client.session.clear()

    def test_retrieve_entries(self):
        """It should return specified number of items, 30 by default."""
        entries = retrieve_entries()
        self.assertEqual(len(entries), 30)
        entries = retrieve_entries(False, 31)
        self.assertEqual(len(entries), 31)

    # Use decorator for patching get function an raise an error
    @patch("scraper.views.requests.get")
    def test_retrieve_entries_exception(self, mock):
        """It should return an empty list when an exception occurs inside the function."""
        # Assign exception to mock
        mock.side_effect = requests.exceptions.HTTPError("HTTP error occurred")
        # Render the view
        self.client.get(reverse("entries"))
        # Get the updated session
        session = self.client.session
        # Check entries were saved
        self.assertIn("entries", session)
        self.assertEqual(len(session.get("entries", [])), 0)

    def test_view_with_session_data(self):
        """It should render the view and save entries in session storage and then retrieve them."""
        session = self.client.session
        # Check session storage is clear
        self.assertNotIn("entries", session)
        # Request the view without filters
        self.client.get(reverse("entries"))
        # Get the updated session
        session = self.client.session
        # Check entries were saved
        self.assertIn("entries", session)
        self.assertEqual(len(session.get("entries", [])), 30)
        # Request the view with filter 1
        self.client.get(f"{reverse("entries")}?{urlencode({"filter":"filter_1"})}")
        # Get the updated session
        session = self.client.session
        # Check entries were saved
        self.assertIn("entries", session)
        # Request the view with filter 2
        self.client.get(f"{reverse("entries")}?{urlencode({"filter":"filter_2"})}")
        # Get the updated session
        session = self.client.session
        # Check entries were saved
        self.assertIn("entries", session)


class TestEntry(TestCase):
    """Class for testing Entry class and a function related."""

    def test_to_int(self):
        """It should cast values correctly."""
        self.assertEqual(to_int(1), 1)
        self.assertEqual(to_int("13"), 13)
        self.assertEqual(to_int("a"), 0)
        self.assertEqual(to_int(True), 0)
        self.assertEqual(to_int(None), 0)

    def test_entry_initialization(self):
        """It should create entry objects."""
        entry = Entry(1, "Title", 2, 3)
        self.assertEqual(entry.number, 1)
        self.assertEqual(entry.title, "Title")
        self.assertEqual(entry.points, 2)
        self.assertEqual(entry.comments, 3)
        entry = Entry("1", 13, "x", True)
        self.assertEqual(entry.number, 1)
        self.assertEqual(entry.title, "13")
        self.assertEqual(entry.points, 0)
        self.assertEqual(entry.comments, 0)

    def test_entry_repr(self):
        entry = Entry(1, "Title", 2, 3)
        self.assertEqual(str(entry), "Entry(1,Title,2,3,1)")

    def test_count_words(self):
        """It should return the aproppriate number of words."""
        entry = Entry(1, "Title with four words", 2, 3)
        self.assertEqual(entry.words, 4)
        entry = Entry(4, "This is - a self-explained example", 5, 6)
        self.assertEqual(entry.words, 5)
        entry = Entry(1, "- -Title- with ? 3", 2, 3)
        self.assertEqual(entry.words, 2)
        entry = Entry(6, "Llama 3.1 Omni Model", 90, 7)
        self.assertEqual(entry.words, 3)

    def test_apply_filter_1(self):
        """It should only return items with more than five words in title."""
        entries = [
            Entry(4, "Comic Mono", 34, 6),
            Entry(6, "Llama 3.1 Omni Model", 90, 7),
            Entry(22, "The Dune Shell", 145, 43),
        ]
        self.assertEqual(len(entries), 3)
        self.assertEqual(len(Entry.apply_filter_1(entries)), 0)
        entries.extend(
            [
                Entry(
                    28,
                    "Knowledge graphs using Ollama and Embeddings to answer and visualizing queries",
                    74,
                    7,
                ),
                Entry(
                    10,
                    "Meticulous (YC S21) is hiring to eliminate UI tests",
                    0,
                    5,
                ),
                Entry(
                    18,
                    "Text makeup – a tool to decode and explore Unicode strings",
                    21,
                    4,
                ),
            ]
        )
        self.assertEqual(len(entries), 6)
        self.assertEqual(len(Entry.apply_filter_1(entries)), 3)

    def test_apply_filter_1_sorting(self):
        """It should sort items by number of comments."""
        entries = [
            Entry(4, "Comic Mono", 34, 6),
            Entry(
                28,
                "Knowledge graphs using Ollama and Embeddings to answer and visualizing queries",
                74,
                7,
            ),
            Entry(
                10,
                "Meticulous (YC S21) is hiring to eliminate UI tests",
                0,
                5,
            ),
            Entry(
                18,
                "Text makeup – a tool to decode and explore Unicode strings",
                21,
                4,
            ),
            Entry(22, "The Dune Shell", 145, 43),
        ]
        filtered_entries = Entry.apply_filter_1(entries)
        self.assertEqual(len(entries), 5)
        self.assertEqual(len(filtered_entries), 3)
        self.assertEqual(filtered_entries[0].number, 18)
        self.assertEqual(filtered_entries[1].number, 10)
        self.assertEqual(filtered_entries[2].number, 28)

    def test_apply_filter_2(self):
        """It should only return items with less than or equal to five words in title."""
        entries = [
            Entry(22, "The Dune Shell New Story", 145, 43),
            Entry(6, "Llama 3.1 Omni Model", 90, 7),
            Entry(4, "Comic Mono", 34, 6),
        ]
        self.assertEqual(len(entries), 3)
        self.assertEqual(len(Entry.apply_filter_2(entries)), 3)
        entries.append(
            Entry(
                10,
                "Meticulous (YC S21) is hiring to eliminate UI tests",
                0,
                0,
            )
        )
        self.assertEqual(len(entries), 4)
        self.assertEqual(len(Entry.apply_filter_2(entries)), 3)

    def test_apply_filter_2_sorting(self):
        """It should sort items by points."""
        entries = [
            Entry(22, "The Dune Shell", 145, 6),
            Entry(6, "Llama 3.1 Omni Model", 90, 43),
            Entry(4, "Comic Mono", 34, 7),
        ]
        filtered_entries = Entry.apply_filter_2(entries)
        self.assertEqual(len(entries), 3)
        self.assertEqual(len(filtered_entries), 3)
        self.assertEqual(filtered_entries[0].number, 4)
        self.assertEqual(filtered_entries[1].number, 6)
        self.assertEqual(filtered_entries[2].number, 22)
        entries.extend(
            [
                Entry(
                    10,
                    "Meticulous (YC S21) is hiring to eliminate UI tests",
                    0,
                    0,
                ),
            ]
        )
        filtered_entries = Entry.apply_filter_2(entries)
        self.assertEqual(len(entries), 4)
        self.assertEqual(len(filtered_entries), 3)
