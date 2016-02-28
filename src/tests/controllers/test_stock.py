from anillo.http.request import Request

from controllers.stock import ListStocks, GetStock, PeDetails

from services.fixtures import _create_stocks_with_data

def test_stocks():
    _create_stocks_with_data()

    request = Request()
    x = ListStocks()
    response = x.get(request)
    assert response['status'] == 200
    assert len(response['body']['stocks']) == 20

    request = Request()
    x = GetStock()
    response = x.get(request, 12)
    assert response['status'] == 200
    assert 1 == len(response['body'])

    request = Request()
    x = PeDetails()
    response = x.get(request)
    assert response['status'] == 200
    assert response['body']['highest']['pk'] > response['body']['lowest']['pk']

