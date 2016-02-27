from sqlalchemy import exists

from repositories.persistence.author import BookTable
from .session import session_manager as sm
from repositories.author import get_author_by_pk


def create_book(author=None, title=None):
    if isinstance(author, int) or isinstance(author, str):
        author = get_author_by_pk(int(author)).first()
    book = BookTable(author=author, title=title)
    sm.session.add(book)
    sm.commit_session()
    return book


def get_all_books():
    return sm.session.query(BookTable).all()


def get_book_by_pk(pk):
    return sm.session.query(BookTable).filter(BookTable.id == pk)


def modify_book(pk, title, author):
    book = get_book_by_pk(pk).first()
    if not book:
        return False, None
    book.title = title if title else book.title
    book.author = author if author else book.author
    sm.session.add(book)
    sm.commit_session()
    return True, book


def delete_book(pk):
    book = sm.session.query(BookTable).filter(BookTable.id == pk).delete()
    return True
