import string


class Entry:
    """Class for handling entries."""

    def __init__(self, number: int, title: string, points: int, comments: int) -> None:
        """Object initialization."""
        self.number = number
        self.title = title
        self.points = points
        self.comments = comments
        self.words = self.__count_words__()

    def __repr__(self) -> str:
        """Custom representation of the class object."""
        return f"Entry({self.number},{self.title},{self.title},{self.points},{self.comments})"

    def __count_words__(self) -> int:
        """Method for counting words and exclude symbols."""
        words = self.title.split()
        valid_words = []
        for word in words:
            if word.replace("-", "").isalnum():
                valid_words.append(word)
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
