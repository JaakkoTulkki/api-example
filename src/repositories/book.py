from sqlalchemy import exists

from repositories.persistence.author import BookTable, TagTable
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


def modify_book(pk, title, author, tags=None):
    book = get_book_by_pk(pk).first()
    if not book:
        return False, None
    book.title = title if title else book.title
    book.author = author if author else book.author
    if tags:
        tags = sm.session.query(TagTable).filter(TagTable.id.in_(tuple(tags))).all()
        book.tags = tags
    sm.session.add(book)
    sm.commit_session()
    return True, book


def delete_book(pk):
    book = sm.session.query(BookTable).filter(BookTable.id == pk).delete()
    return True

def create_tag(tag=None):
    (tag_exists, ), = sm.session.query(exists().where(TagTable.tag==tag))
    if not tag_exists:
        t = TagTable(tag=tag)
        sm.session.add(t)
        sm.commit_session()
    else:
        t = sm.session.query(TagTable).filter_by(tag=tag).first()
    return True, t


def list_all_tags():
    return sm.session.query(TagTable).all()

def get_tag_by_pk(pk):
    tag = sm.session.query(TagTable).filter(TagTable.id == pk).first()
    return tag

def add_tag_to_book(book, tag):
    book.tags.append(tag)
    sm.session.add(book)
    sm.commit_session()
    return book
