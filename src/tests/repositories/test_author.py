from repositories.persistence.author import AuthorTable
from repositories.author import create_author
from repositories.session import session_manager as sm

def test_create_author_entity():
    data ={
        'first_name': "Ernest",
    }

    author = create_author(**data)
    assert(author.first_name == data['first_name'])

    assert(author.id == 1)

    ernest = sm.session.query(AuthorTable).filter_by(first_name=data['first_name']).first()
    assert(ernest.first_name == data['first_name'])

    assert author is ernest

