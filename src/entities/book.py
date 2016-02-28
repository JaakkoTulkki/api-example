from .entity import Entity


class Book(Entity):
    def __init__(self, book):
        self.pk = book.id
        self.title = book.title
        self.author = book.author.id
        self.tagged_ones = self.tag(book.tags)

    def tag(self, tags):
        self.tags = [Tag(t).toJSONDict() for t in tags] if tags else []

    def __repr__(self):
        return "{} {}".format(self.title)

    def toJSONDict(self):
        l = ['title', 'pk', 'author', 'tags']
        return super().toJSONDict(l)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Tag(Entity):
    def __init__(self, tag_instance):
        self.tag = tag_instance.tag
        self.pk = tag_instance.id

    def __repr__(self):
        return "{} {}".format(self.tag)

    def toJSONDict(self):
        l = ['tag', 'pk']
        return super().toJSONDict(l)

    def __eq__(self, other):
        return self.tag == other.tag