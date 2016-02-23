from repositories.persistence.author import AuthorTable
from .session import session_manager as sm


def create_author(first_name):
    author = AuthorTable(first_name=first_name)
    sm.session.add(author)
    sm.session.commit()
    return author