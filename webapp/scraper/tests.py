from django.test import TestCase
from django.urls import reverse
from .models import Entry
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
    """Class for testing Entry class."""

    def test_entry_initialization(self):
        """Test entry object initialization."""
        entry = Entry(1, "Title", 2, 3)
        self.assertEqual(entry.number, 1)
        self.assertEqual(entry.title, "Title")
        self.assertEqual(entry.points, 2)
        self.assertEqual(entry.comments, 3)

    def test_count_words(self):
        """Test count_words method ."""
        entry = Entry(1, "Title with four words", 2, 3)
        self.assertEqual(entry.words, 4)
        entry = Entry(4, "This is - a self-explained example", 5, 6)
        self.assertEqual(entry.words, 5)
        entry = Entry(1, "- -Title- with ? 3", 2, 3)
        self.assertEqual(entry.words, 2)
        entry = Entry(number=6, title="Llama 3.1 Omni Model", points=90, comments=7)
        self.assertEqual(entry.words, 3)

    def test_apply_filter_1(self):
        """Test apply_filter_1 method only returns items with more than five words in title."""
        entries = [
            Entry(number=4, title="Comic Mono", points=34, comments=6),
            Entry(number=6, title="Llama 3.1 Omni Model", points=90, comments=7),
            Entry(number=22, title="The Dune Shell", points=145, comments=43),
        ]
        filtered_entries = Entry.apply_filter_1(entries)
        self.assertEqual(len(entries), 3)
        self.assertEqual(len(filtered_entries), 0)
        entries.extend(
            [
                Entry(
                    number=28,
                    title="Knowledge graphs using Ollama and Embeddings to answer and visualizing queries",
                    points=74,
                    comments=7,
                ),
                Entry(
                    number=10,
                    title="Meticulous (YC S21) is hiring to eliminate UI tests",
                    points=0,
                    comments=5,
                ),
                Entry(
                    number=18,
                    title="Text makeup – a tool to decode and explore Unicode strings",
                    points=21,
                    comments=4,
                ),
            ]
        )
        self.assertEqual(len(entries), 6)
        self.assertEqual(len(Entry.apply_filter_1(entries)), 3)

    def test_apply_filter_1_sorting(self):
        """Test apply_filter_1 method sorts items by number of comments."""
        entries = [
            Entry(number=4, title="Comic Mono", points=34, comments=6),
            Entry(
                number=28,
                title="Knowledge graphs using Ollama and Embeddings to answer and visualizing queries",
                points=74,
                comments=7,
            ),
            Entry(
                number=10,
                title="Meticulous (YC S21) is hiring to eliminate UI tests",
                points=0,
                comments=5,
            ),
            Entry(
                number=18,
                title="Text makeup – a tool to decode and explore Unicode strings",
                points=21,
                comments=4,
            ),
            Entry(number=22, title="The Dune Shell", points=145, comments=43),
        ]
        filtered_entries = Entry.apply_filter_1(entries)
        self.assertEqual(len(entries), 5)
        self.assertEqual(len(filtered_entries), 3)
        self.assertEqual(filtered_entries[0].number, 18)
        self.assertEqual(filtered_entries[1].number, 10)
        self.assertEqual(filtered_entries[2].number, 28)

    def test_apply_filter_2(self):
        """Test apply_filter_2 method only returns items with less than or equal to five words in title."""
        entries = [
            Entry(number=22, title="The Dune Shell New Story", points=145, comments=43),
            Entry(number=6, title="Llama 3.1 Omni Model", points=90, comments=7),
            Entry(number=4, title="Comic Mono", points=34, comments=6),
        ]
        self.assertEqual(len(entries), 3)
        self.assertEqual(len(Entry.apply_filter_2(entries)), 3)
        entries.append(
            Entry(
                number=10,
                title="Meticulous (YC S21) is hiring to eliminate UI tests",
                points=0,
                comments=0,
            )
        )
        self.assertEqual(len(entries), 4)
        self.assertEqual(len(Entry.apply_filter_2(entries)), 3)

    def test_apply_filter_2_sorting(self):
        """Test apply_filter_2 method sorts items by points."""
        entries = [
            Entry(number=22, title="The Dune Shell", points=145, comments=43),
            Entry(number=6, title="Llama 3.1 Omni Model", points=90, comments=7),
            Entry(number=4, title="Comic Mono", points=34, comments=6),
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
                    number=10,
                    title="Meticulous (YC S21) is hiring to eliminate UI tests",
                    points=0,
                    comments=0,
                ),
            ]
        )
        filtered_entries = Entry.apply_filter_2(entries)
        self.assertEqual(len(entries), 4)
        self.assertEqual(len(filtered_entries), 3)


class ViewTest(TestCase):
    def test_retrieve_entries(self):
        """Test retrieve_entries function returns only 30 items."""
        entries = retrieve_entries()
        self.assertEqual(len(entries), 30)
