import datetime

from repositories.persistence.author import AuthorTable, BookTable, TagTable
from repositories.author import create_author, create_book, create_tag
from repositories.session import session_manager as sm

DATA = data ={
        'first_name': "Dude",
        'last_name': 'Some',
        'birth_date': datetime.date(year=1900, day=2, month=7),
        'date_of_death': datetime.date(year=1976, day=5, month=7)
    }

def test_create_author_entity():
    data ={
        'first_name': "Ernest",
        'last_name': 'Hemingway',
    }

    author = create_author(**data)
    assert(author.first_name == data['first_name'])
    assert(author.id == 1)

    ernest = sm.session.query(AuthorTable).filter_by(first_name=data['first_name']).first()
    assert(ernest.first_name == data['first_name'])
    assert author is ernest

    # add birthday
    bday = datetime.date(year=1900, day=2, month=7)
    ernest.birth_date = bday
    death_day = datetime.date(1959, day=30, month=8)
    ernest.date_of_death = death_day
    sm.commit_session()

    ernest = sm.session.query(AuthorTable).filter_by(first_name=data['first_name']).first()
    assert ernest.birth_date == bday
    assert ernest.date_of_death != bday


def test_create_books_with_tags():
    author = create_author(**DATA)
    book = create_book(author=author, title="My Little Pony")
    assert isinstance(book, BookTable)

    assert book.author is author
    assert book.title == "My Little Pony"

    book_in_db = sm.session.query(BookTable).filter_by(title="My Little Pony").first()
    assert book_in_db is book

    # create another book
    second_book = create_book(author=author, title="Chicken in the farm")

    assert len(author.books) == 2
    assert author.books[0] is book
    assert author.books[1] is second_book

    # time to create tags for the book
    tag = create_tag(tag="romance")
    tag.books.append(book)
    tag.books.append(second_book)
    sm.session.add(tag)
    sm.commit_session()

    tag = sm.session.query(TagTable).filter_by(tag="romance").first()
    assert len(tag.books) == 2
    assert book in tag.books

    # create another tag
    second_tag = create_tag(tag="horror")
    second_tag.books.append(book)
    sm.session.add(second_tag)
    sm.commit_session()

    book = sm.session.query(BookTable).filter_by(title=book.title).first()
    assert len(book.tags) == 2
    assert sorted([t.tag for t in book.tags]) == ['horror', 'romance']






