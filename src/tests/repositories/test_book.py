from repositories.author import create_author
from repositories.book import create_book, get_all_books, get_book_by_pk, modify_book, delete_book

def test_create_book():
    data ={
        'first_name': "Ernest",
        'last_name': 'Hemingway',
    }
    author = create_author(**data)

    chicken_book = create_book(author, "Stories of a Lonely Chicken")
    assert chicken_book

    man_book = create_book(author, "Man and the Sea")

    y_book = create_book(author.id, "xyz")
    assert y_book.author is author

    books = sorted([book for book in get_all_books()], key=lambda x: x.title)

    assert man_book is books[0]
    assert chicken_book is books[1]

    book = get_book_by_pk(man_book.id)
    assert man_book is book.first()

    data ={
        'first_name': "Winston",
        'last_name': 'Churchill',
    }
    second_author = create_author(**data)

    modified, book = modify_book(book.first().id, author=second_author, title="new title")
    assert modified
    assert book.author.first_name == "Winston"
    assert book.title == "new title"

    pk = book.id
    deleted = delete_book(pk)
    assert deleted
    book = get_book_by_pk(pk).first()
    assert not book






