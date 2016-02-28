from sqlalchemy import Column, Integer, Text, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from repositories.config import Base

class StockTable(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    name = Column(String, nullable=False)
    number_of_stocks = Column(Integer, nullable=False)
    financial = relationship("FinancialDataTable", uselist=False, back_populates="stock")

class FinancialDataTable(Base):
    __tablename__ = "financial"
    id = Column(Integer, primary_key=True)
    profit = Column(Integer, nullable=False)
    book_value = Column(Integer, nullable=False)
    dividend = Column(Float, nullable=False)
    market_value = Column(Integer)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = relationship("StockTable", back_populates="financial")

