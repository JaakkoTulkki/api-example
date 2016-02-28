from entities.book import Book, Tag

from repositories.book import create_book, get_all_books, get_book_by_pk, modify_book,\
    delete_book, create_tag, list_all_tags, add_tag_to_book, get_tag_by_pk
from repositories.author import get_author_by_pk
from repositories.persistence.author import AuthorTable

def create_book_service(author, title):
    book = create_book(author, title)
    if book:
        book = Book(book)
        return True, book, {}
    return False, None, {'msg': "No book could be created"}


def get_all_books_service():
    books = []
    for book in get_all_books():
        books.append(Book(book))
    return True, books, {}


def get_book_by_pk_service(pk):
    book = get_book_by_pk(pk).first()
    if book:
        book = Book(book)
        return True, book, {}
    else:
        return False, None, {"msg": "No book found"}


def modify_book_service(pk, author=None, title=None, tags=None):
    book = get_book_by_pk(pk).first()
    if not book:
        return False, None, {'msg': "No book found"}
    if not isinstance(author, AuthorTable):
        author = get_author_by_pk(author).first()
    t, book = modify_book(book.id, author=author, title=title, tags=tags)
    book = Book(book)
    return True, book, {}


def delete_book_service(pk):
    delete_book(pk)
    return True, None, {}


def create_tag_service(tag=None):
    if tag:
        created, tag = create_tag(tag)
        tag = Tag(tag)
        return created, tag, {}
    return False, None, {'msg': "No tag provided"}


def list_tags_service():
    tags = list_all_tags()
    tags = [Tag(tag) for tag in tags]
    return True, tags, {}

def add_tag_to_book_service(book_pk, tag_id):
    book = get_book_by_pk(book_pk).first()
    tag = get_tag_by_pk(tag_id)
    add_tag_to_book(book, tag)
    return True, book, {}

def get_tag_books_pk_service(pk):
    tag = get_tag_by_pk(pk)
    result = [Book(book) for book in tag.books]
    return True, {tag.tag: result}, {}
