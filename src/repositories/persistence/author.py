from sqlalchemy import Column, Date, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from repositories.config import Base

book_tag_association_table = Table('association', Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('booktag_id', Integer, ForeignKey('booktag.id'))
)


class AuthorTable(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    birth_date = Column(Date)
    date_of_death = Column(Date)
    books = relationship("BookTable", back_populates="author")


class BookTable(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    author_id = Column(Text, ForeignKey('author.id'))
    author = relationship("AuthorTable", back_populates="books")
    title = Column(Text, nullable=False)
    tags = relationship(
        "TagTable",
        secondary=book_tag_association_table,
        back_populates="books")


class TagTable(Base):
    __tablename__ = "booktag"

    id = Column(Integer, primary_key=True)
    tag = Column(Text, unique=True)
    books = relationship(
        "BookTable",
        secondary=book_tag_association_table,
        back_populates="tags")


