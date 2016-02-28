from .entity import Entity

class Stock(Entity):
    def __init__(self, stock):
        self.s = stock
        self.pk = stock.id
        self.name = stock.name
        self.ticker = stock.ticker
        self.number_of_stocks = stock.number_of_stocks
        self.financial = stock.financial
        self.calc_market_value()
        self.calc_book_value_per_share()
        self.calc_dividend()
        self.calc_dividend_yield()
        self.calc_pe()


    def calc_market_value(self):
        self.share_price = self.financial.market_value / self.number_of_stocks

    def calc_book_value_per_share(self):
        self.book_price_per_share = self.financial.book_value / self.number_of_stocks

    def calc_dividend(self):
        self.dividend = self.financial.dividend /self.number_of_stocks

    def calc_dividend_yield(self):
        self.dividend_yield = self.dividend / self.share_price * 100

    def calc_pe(self):
        self.pe = self.share_price / (self.financial.profit / self.number_of_stocks)

    def __repr__(self):
        return "{} ({}): {}".format(self.name, self.ticker, self.share_price)

    def toJSONDict(self):
        l = ['pk', 'name', 'ticker', 'number_of_stocks', 'share_price', 'book_price_per_share',
             'dividend', 'dividend_yield', 'pe']
        return super().toJSONDict(l)

