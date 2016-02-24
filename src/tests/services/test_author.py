from services.author import create_author_service

def test_create_author_service():
    data = {
        'first_name': "John",
        'last_name': 'Irving',
    }
    created, author, errors = create_author_service(**data)
    assert created
    assert not errors
    assert author.toJSONDict() == data

    created, author, errors = create_author_service(**data)
    assert not created
    assert errors
    assert author == None