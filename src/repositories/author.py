from sqlalchemy import exists

from repositories.persistence.author import AuthorTable, BookTable, TagTable
from .session import session_manager as sm


def create_author(first_name, last_name=None, birth_date=None, date_of_death=None):
    author = AuthorTable(first_name=first_name, last_name=last_name, birth_date=birth_date, date_of_death=date_of_death)
    sm.session.add(author)
    sm.session.commit()
    return author


def get_all_authors():
    return sm.session.query(AuthorTable).all()


def get_author_by_name(first_name, last_name):
    data = {
        'first_name': first_name,
        'last_name': last_name
    }
    return _filter_author(**data)

def get_author_by_pk(pk):
    q = sm.session.query(AuthorTable).filter(AuthorTable.id == pk)
    return q

def update_author(author, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
    author.first_name = first_name if first_name else "" if first_name == "" else author.first_name
    author.last_name = last_name if last_name else "" if first_name == "" else author.last_name
    author.birth_date = date_of_birth if date_of_birth else "" if date_of_birth == "" else author.birth_date
    author.date_of_death = date_of_death if date_of_death else "" if date_of_birth == "" else author.date_of_death
    sm.session.add(author)
    sm.commit_session()
    return author

def _filter_author(**kwargs):
    return sm.session.query(AuthorTable).filter_by(**kwargs)


def delete_author(pk):
    author = get_author_by_pk(pk)
    if not author.first():
        return False
    author.delete()
    sm.commit_session()
    return True