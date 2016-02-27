from .entity import Entity


class Book(Entity):
    def __init__(self, book_id, title, author_id):
        self.pk = book_id
        self.title = title
        self.author = author_id

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def toJSONDict(self):
        l = ['title', 'pk', 'author']
        return super().toJSONDict(l)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author