import datetime

from repositories.session import session_manager
from repositories.user import create_user
from repositories.author import create_author
from repositories.book import create_book, create_tag, modify_book
from repositories.session import session_manager as sm
from repositories.persistence.stock import StockTable, FinancialDataTable

import random
import string

def load_fixtures():
    session_manager.create_session()

    _load_users_fixtures()

    _create_stocks_with_data()

    session_manager.commit_session()
    session_manager.close_session()


def _load_users_fixtures():
    create_user('jimena@test.com', 'abc12345', '8c99f50fcb424c66b6e489d15461b782')
    create_user('nikolai@test.com', 'abc12345', '9942eb5913c54f2eae5353e6b43324fb')

    e = create_author("Ernest", "Hemingway", datetime.date(1899, 3, 20), datetime.date(1950, 6, 7))
    d = create_author("Fjodor", "Dostoyevski", datetime.date(1800, 3, 30), datetime.date(1876, 1, 11))

    bells = create_book(e, "To Whom the Bell Toll")
    man = create_book(e, "Man and the Sea")

    crime = create_book(d, "Crime and Punishment")
    gambler = create_book(d, "The Gambler")

    t, crime_tag = create_tag("crime")
    t, classic_tag = create_tag("classic")

    modify_book(bells.id, None, None, [crime_tag.id, classic_tag.id])

    modify_book(man.id, None, None, [crime_tag.id, classic_tag.id])
    modify_book(crime.id, None, None, [crime_tag.id, classic_tag.id])

    modify_book(gambler.id, None, None, [crime_tag.id])
    modify_book(gambler.id, None, None, [classic_tag.id])



def _create_stocks_with_data():
    for e in range(20):
        stock = StockTable()
        stock.ticker = "".join(random.choice(string.ascii_lowercase) for i in range(4))
        stock.name = "".join(random.choice(string.ascii_uppercase) for i in range(12))
        stock.number_of_stocks = random.randint(100, 1000)

        financial = FinancialDataTable()
        financial.profit = random.randint(-10, 10000)
        financial.book_value = random.randint(100, 10000)
        financial.dividend = random.randint(33, 66)/100*(financial.profit / stock.number_of_stocks)
        financial.market_value = financial.profit * random.randint(3, 25)
        if financial.market_value < 0:
            financial.market_value * -1

        stock.financial = financial

        sm.session.add(stock, financial)
        sm.commit_session()
