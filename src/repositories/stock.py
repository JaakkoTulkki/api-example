from .session import session_manager as sm
from repositories.persistence.stock import StockTable, FinancialDataTable


def list_all_stocks():
    return sm.session.query(StockTable).all()


def get_one_stock_by_pk(pk):
    return sm.session.query(StockTable).filter(StockTable.id == pk).first()


