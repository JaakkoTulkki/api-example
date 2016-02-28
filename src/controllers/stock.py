from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from controllers.utils import convert_body_to_dict

from services.stock import list_all_stocks_service, get_one_stock_by_pk_service, get_highest_pe_service,\
    get_lowest_pe_service


class ListStocks(Controller):
    def get(self, request):
        ok, stocks, errors = list_all_stocks_service()
        if errors:
            return BadRequest({'msg': "could not get stocks"})
        return Ok({'stocks': [stock.toJSONDict() for stock in stocks]})


class GetStock(Controller):
    def get(self, request, pk):
        ok, stock, errors = get_one_stock_by_pk_service(pk)
        if errors:
            return BadRequest({'msg': "Could not get stock"})
        return Ok({'stocks': stock.toJSONDict()})


class PeDetails(Controller):
    def get(self, request):
        ok, low_pe, errors = get_lowest_pe_service()
        if errors:
            return BadRequest({'msg': "Could not get data"})
        ok, high_pe, errors = get_highest_pe_service()
        if errors:
            return BadRequest({'msg': "Could not get data"})
        return Ok({'highest':high_pe, 'lowest': low_pe})