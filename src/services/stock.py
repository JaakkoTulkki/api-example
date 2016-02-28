from repositories.stock import list_all_stocks, get_one_stock_by_pk

from entities.stock import Stock

def list_all_stocks_service():
    stocks = [Stock(stock) for stock in list_all_stocks()]
    return True, stocks, {}


def get_one_stock_by_pk_service(pk):
    stock = Stock(get_one_stock_by_pk(pk))
    return True, stock, {}

def get_lowest_pe_service():
    stocks = list_all_stocks()
    lowest = min([Stock(stock).toJSONDict() for stock in stocks], key=lambda x: x['pe'])
    return True, lowest, {}


def get_highest_pe_service():
    stocks = list_all_stocks()
    highest = max([Stock(stock).toJSONDict() for stock in stocks], key=lambda x: x['pe'])
    return True, highest, {}