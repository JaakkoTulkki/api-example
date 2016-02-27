from entities.book import Book

from repositories.book import create_book, get_all_books, get_book_by_pk, modify_book, delete_book
from repositories.author import get_author_by_pk
from repositories.persistence.author import AuthorTable

def create_book_service(author, title):
    book = create_book(author, title)
    if book:
        book = Book(book_id=book.id, title=book.title, author_id=author if type(author) is int else author.id)
        return True, book, {}
    return False, None, {'msg': "No book could be created"}


def get_all_books_service():
    books = []
    for book in get_all_books():
        books.append(Book(book_id=book.id, title=book.title, author_id=book.author.id))
    return True, books, {}


def get_book_by_pk_service(pk):
    book = get_book_by_pk(pk).first()
    if book:
        book = Book(book_id=book.id, title=book.title, author_id=book.author.id)
        return True, book, {}
    else:
        return False, None, {"msg": "No book found"}


def modify_book_service(pk, author=None, title=None):
    book = get_book_by_pk(pk).first()
    if not book:
        return False, None, {'msg': "No book found"}
    if not isinstance(author, AuthorTable):
        author = get_author_by_pk(author).first()
    t, book = modify_book(book.id, author=author, title=title)
    book = Book(book_id=book.id, title=book.title, author_id=book.author.id)
    return True, book, {}


def delete_book_service(pk):
    delete_book(pk)
    return True, None, {}
