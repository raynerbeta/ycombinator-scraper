class Entry:
    """Class for handling entries."""

    def __init__(self, number, title, points, comments) -> None:
        """Object initialization."""
        self.number = number
        self.title = title
        self.points = points
        self.comments = comments

    def __repr__(self) -> str:
        """Custom representation of the class object."""
        return f"Entry({self.number},{self.title},{self.title},{self.points},{self.comments})"

    def to_dict(self):
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
