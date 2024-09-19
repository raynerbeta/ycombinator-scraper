import string
import copy


def to_int(value) -> int:
    """Function for casting a given value into an int.
    Only tries conversion when a string is provided.
    If an exception occurs or type is anything but string, returns 0."""
    t = type(value)
    if t == int:
        return value
    if t == str:
        try:
            return int(value)
        except:
            return 0
    else:
        return 0


class Entry:
    """Class for handling entries."""

    def __init__(self, number: int, title: string, points: int, comments: int) -> None:
        """Object initialization."""
        self.number = to_int(number)
        self.title = str(title)
        self.points = to_int(points)
        self.comments = to_int(comments)
        self.words = self.__count_words__()

    def __repr__(self) -> str:
        """Custom representation of the class object."""
        return f"Entry({self.number},{self.title},{self.title},{self.points},{self.comments})"

    def __count_words__(self) -> int:
        """Method for counting words and exclude symbols."""
        # Split title into words based on spaces
        words = self.title.split()
        # Use list comprehension for evaluating each word
        # And only adding valid words (that contains at least 1 alphabetic character)
        valid_words = [word for word in words if any(char.isalpha() for char in word)]
        return len(valid_words)

    def to_dict(self) -> dict:
        """Method for yielding a dictionary from the object."""
        return {
            "number": self.number,
            "title": self.title,
            "points": self.points,
            "comments": self.comments,
        }

    @classmethod
    def from_dict(cls, data):
        """Class method for yielding an Entry object from a dictionary."""
        return cls(
            number=data["number"],
            title=data["title"],
            points=data["points"],
            comments=data["comments"],
        )

    @classmethod
    def apply_filter_1(cls, data):
        """
        Method for filtering entries with more than five words in the title
        and ordering by the number of comments.
        """
        entries = copy.deepcopy(data)
        entries = filter(lambda entry: entry.words > 5, entries)
        entries = sorted(
            entries,
            key=lambda entry: entry.comments,
        )
        return entries

    @classmethod
    def apply_filter_2(cls, data):
        """
        Method for filtering entries with less than or equal to five words in the title
        and ordering by points.
        """
        entries = copy.deepcopy(data)
        entries = filter(lambda entry: entry.words <= 5, entries)
        entries = sorted(entries, key=lambda entry: entry.points)
        return entries
