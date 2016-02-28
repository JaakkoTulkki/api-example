from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from controllers.utils import convert_body_to_dict

from services.book import get_all_books_service, get_book_by_pk_service, delete_book_service,\
    modify_book_service, create_book_service, create_tag_service, list_tags_service,\
    get_tag_books_pk_service


class CreateListBook(Controller):
    def get(self, request):
        ok, books, errors = get_all_books_service()
        if errors:
            return BadRequest(errors)
        books = [book.toJSONDict() for book in books] if books else []
        return Ok({'books': books})

    def post(self, request):
        data = convert_body_to_dict(request['body'])
        ok, book, errors = create_book_service(**data)
        if errors:
            return BadRequest(errors)
        return Ok({'book': book.toJSONDict()})


class DetailUpdateDeleteBook(Controller):
    def get(self, request, pk=None):
        ok, book, errors = get_book_by_pk_service(pk)
        if errors:
            return BadRequest(errors)
        return Ok({'book': book.toJSONDict()})

    def put(self, request, pk):
        data = convert_body_to_dict(request['body'])
        ok, book, errors = modify_book_service(pk, **data)
        if errors:
            return BadRequest(errors)
        return Ok({'book': book.toJSONDict()})

    def delete(self, request, pk):
        delete_book_service(pk)
        return Ok({'msg': "deleted"})

class ListCreateTag(Controller):
    def get(self, request):
        ok, tags, errors = list_tags_service()
        return Ok({'tags': [t.toJSONDict() for t in tags]})

    def post(self, request):
        data = convert_body_to_dict(request['body'])
        ok, tag, errors = create_tag_service(**data)
        if errors:
            return BadRequest(errors)
        return Ok({'tag': tag.toJSONDict()})

class DetailTag(Controller):
    def get(self, request, pk):
        ok, tag_books_dict, errors = get_tag_books_pk_service(pk)
        if errors:
            return BadRequest(errors)
        result = [book.toJSONDict() for k in tag_books_dict.keys() for book in tag_books_dict[k]]
        return Ok({pk: result})
