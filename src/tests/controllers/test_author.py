from anillo.http.request import Request

from controllers.author import ListCreateAuthors, DetailUpdateDeleteAuthor

def test_post_list_authors():
    request = Request()
    data = {
        'first_name': "Linus",
        "last_name": "Torvalds"
    }
    request['body'] = data

    x = ListCreateAuthors()
    response = x.post(request)

    assert response['status'] == 200

    # try to create a duplicate
    x = ListCreateAuthors()
    response = x.post(request)
    assert response['status'] == 400

def test_detail_update_delete_author():
    request = Request()
    # create author to view details
    data = {
        'first_name': "George",
        "last_name": "Bush"
    }
    request['body'] = data

    x = ListCreateAuthors()
    response = x.post(request)
    assert response['status'] == 200

    pk = response['body']['author'][0]['pk']
    url = "authors/{}"
    request = Request()
    x = DetailUpdateDeleteAuthor()
    response = x.get(request, pk)
    assert response['body']['author'][0]['pk'] == pk

    # update data
    request = Request()
    x = DetailUpdateDeleteAuthor()
    request['body'] = {
        'first_name': "Barack",
        "last_name": "Obama"
    }
    response = x.put(request, pk)
    assert response['status'] == 200

    # check all data changed
    request = Request()
    x = DetailUpdateDeleteAuthor()
    response = x.get(request, pk)
    assert response['body']['author'][0]['first_name'] == "Barack"

    # delete it
    request = Request()
    x = DetailUpdateDeleteAuthor()
    response = x.delete(request, pk)
    assert response['status'] == 200
    # check does not exist anymore
    request = Request()
    x = DetailUpdateDeleteAuthor()
    response = x.get(request, pk)
    assert response['status'] == 400





