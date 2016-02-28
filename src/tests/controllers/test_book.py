from anillo.http.request import Request

from controllers.book import CreateListBook, DetailUpdateDeleteBook, ListCreateTag
from services.author import create_author_service

def test_create_list_book():
    data = {
        'first_name': "John",
        "last_name": "Fogerty"
    }
    g, author, e = create_author_service(**data)

    data = {
        "author": author.pk,
        "title": "Revolution"
    }

    request = Request()
    request['body'] = data
    x = CreateListBook()
    response = x.post(request)
    assert response['status'] == 200

    data['title'] = "Revolution vol.2"
    request = Request()
    request['body'] = data
    x = CreateListBook()
    response = x.post(request)
    assert response['status'] == 200

    request = Request()
    x = CreateListBook()
    response = x.get(request)
    assert response['status'] == 200
    assert len(response['body']['books']) == 2

def test_detail_update_delete_book_and_tags():
    data = {
        'first_name': "D",
        "last_name": "Fogerty"
    }
    g, author, e = create_author_service(**data)

    data = {
        'first_name': "D",
        "last_name": "D"
    }
    g, second_author, e = create_author_service(**data)

    data = {
        "author": author.pk,
        "title": "Revolution vol3"
    }

    request = Request()
    request['body'] = data
    x = CreateListBook()
    response = x.post(request)
    assert response['status'] == 200
    book_pk = response['body']['book']['pk']

    # create two tags and add it to the book
    request = Request()
    request['body'] = {'tag': "romance"}
    x = ListCreateTag()
    response = x.post(request)
    assert response['status'] == 200
    romance_tag = response['body']['tag']['pk']

    request = Request()
    request['body'] = {'tag': "horror"}
    x = ListCreateTag()
    response = x.post(request)
    assert response['status'] == 200
    horror_tag = response['body']['tag']['pk']

    request = Request()
    x = ListCreateTag()
    response = x.get(request)
    assert response['status'] == 200
    assert len(response['body']['tags']) == 2


    request = Request()
    x = DetailUpdateDeleteBook()
    response = x.get(request, book_pk)
    assert response['status'] == 200
    assert response['body']['book']['title'] == "Revolution vol3"

    request = Request()
    data['author'] = second_author.pk
    data['title'] = "wow"
    # now add the tags
    data['tags'] = [romance_tag, horror_tag]
    request['body'] = data
    x = DetailUpdateDeleteBook()
    response = x.put(request, book_pk)
    assert response['status'] == 200
    assert response['body']['book']['author'] == second_author.pk
    assert response['body']['book']['title'] == "wow"
    assert sorted([t['tag'] for t in response['body']['book']['tags']]) == ['horror', 'romance']

    request = Request()
    x = DetailUpdateDeleteBook()
    response = x.delete(request, book_pk)
    assert response['status'] == 200

    # make sure does not exist
    request = Request()
    x = DetailUpdateDeleteBook()
    response = x.get(request, book_pk)
    assert response['status'] == 400
    assert response['body']['msg'].startswith("No book found")



