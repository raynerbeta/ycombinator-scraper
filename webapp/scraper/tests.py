from django.test import TestCase
from django.urls import reverse
from .models import Entry, to_int
from .views import retrieve_entries

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
            Entry(22, "The Dune Shell", 145, 43),
            Entry(6, "Llama 3.1 Omni Model", 90, 7),
            Entry(4, "Comic Mono", 34, 6),
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


class ViewTest(TestCase):
    def test_retrieve_entries(self):
        """It should only return 30 items."""
        entries = retrieve_entries()
        self.assertEqual(len(entries), 30)
