from django.db import models

# Create your models here.
class Entry():
    def __init__(self, number, title, points, comments) -> None:
        self.number = number
        self.title = title
        self.points = points
        self.comments = comments