from sqlalchemy import Column, Date, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from repositories.config import Base

# book_tag_association_table = Table('association', Base.metadata,
#     Column('book_id', Integer, ForeignKey('book.id')),
#     Column('tag_id', Integer, ForeignKey('tag.id'))
# )


class AuthorTable(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    # last_name = Column(Text)
    # birth_date = Column(Date)
    # date_of_death = Column(Date, nullable=True)
    # books = relationship("BookTable", back_populates="author")
#
#
# class BookTable(Base):
#     __tablename__ = "book"
#
#     id = Column(Integer, primary_key=True)
#     author_id = Column(Text, ForeignKey('author.id'))
#     author = relationship("AuthorTable", back_populates="books")
#     title = Column(Text)
#     description = Column(Text)
#     year_published = Column(Integer, nullable=True)
#     tags = relationship(
#         "TagTable",
#         secondary=book_tag_association_table,
#         back_populates="books")
#
#
# class TagTable(Base):
#     __tablename__ = "booktag"
#
#     id = Column(Integer, primary_key=True)
#     tag = Column(Text, unique=True)
#     books = relationship(
#         "BookTable",
#         secondary=book_tag_association_table,
#         back_populates="tags")
#
#
