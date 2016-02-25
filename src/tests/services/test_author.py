from services.author import create_author_service, delete_author_service, modify_author_service,\
    get_author_by_pk_service, get_all_authors_service
from repositories.author import get_author_by_name

import datetime

def test_create_author_service_and_get_author_service():
    data = {
        'first_name': "John",
        'last_name': 'Irving',
    }
    created, author, errors = create_author_service(**data)
    assert created
    assert not errors
    d = author.toJSONDict()
    del d['pk']
    assert d == data

    created, try_again_author, errors = create_author_service(**data)
    assert not created
    assert errors
    assert try_again_author == None

    got_it, get_author, errors = get_author_by_pk_service(author.pk)
    assert got_it
    assert get_author.toJSONDict() == author.toJSONDict()


def test_update_author_service_and_get_all_authors():
    data = {
        'first_name': "John",
        'last_name': 'Lennon',
    }
    created, author, errors = create_author_service(**data)
    day = datetime.date(year=1946, day=23, month=11)
    created, author, errors = modify_author_service(author.pk, first_name="Yoko", last_name="Ono", date_of_birth=day)
    a = get_author_by_name("Yoko", "Ono").first()
    g, a, errors = get_author_by_pk_service(a.id)
    assert a == author
    assert a.date_of_birth == '23-11-1946'

    created, author, errors = create_author_service(**data)
    assert created
    g, all_authors, errors = get_all_authors_service()
    authors = sorted([a.first_name for a in all_authors])
    assert len(authors) == 2
    assert authors == ["John", "Yoko"]



def test_delete_author_service():
    data = {
        'first_name': "Jamie",
        'last_name': 'Oliver',
    }
    created, author, errors = create_author_service(**data)
    deleted, author, errors = delete_author_service(author.pk)
    assert deleted
    jamie = get_author_by_name("Jamie", "Oliver").first()
    assert not jamie