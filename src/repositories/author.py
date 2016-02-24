from sqlalchemy import exists

from repositories.persistence.author import AuthorTable, BookTable, TagTable
from .session import session_manager as sm



def create_author(first_name, last_name=None, birth_date=None, date_of_death=None):
    author = AuthorTable(first_name=first_name, last_name=last_name, birth_date=birth_date, date_of_death=date_of_death)
    sm.session.add(author)
    sm.session.commit()
    return author

def create_book(author=None, title=None):
    book = BookTable(author=author, title=title)
    sm.session.add(book)
    sm.commit_session()
    return book

def create_tag(tag=None):
    (tag_exists, ), = sm.session.query(exists().where(TagTable.tag==tag))
    if not tag_exists:
        t = TagTable(tag=tag)
        sm.session.add(t)
        sm.commit_session()
    else:
        t = sm.session.query(TagTable).filter_by(tag=tag).first()
    return t



