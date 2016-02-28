from anillo.handlers.routing import optionized_url as url, context


from controllers.index import Index
from controllers.user import Login, Register, List
from controllers.author import ListCreateAuthors, DetailUpdateDeleteAuthor
from controllers.book import CreateListBook, DetailUpdateDeleteBook, ListCreateTag

urls = [
    context("/api/v1", [
        url("/", Index(), methods=["get", "post"]),
        url("/login", Login(), methods=["post"]),
        url("/users", Register(), methods=["post"]),
        url("/users", List(), methods=["get"]),
        url("/authors", ListCreateAuthors(), methods=["get", "post"]),
        url("/authors/<int:pk>", DetailUpdateDeleteAuthor(), methods=["get", "delete", "put"]),
        url("/books", CreateListBook(), methods=["get", "post"]),
        url("/books/<int:pk>", DetailUpdateDeleteBook(), methods=["get", "delete", "put"]),
        url("/tags", CreateListBook(), methods=["get", "post"]),

    ]),
]
