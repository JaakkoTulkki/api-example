from anillo.http import Ok, BadRequest

from controllers.controller import Controller

from services.author import get_all_authors_service, create_author_service, get_author_by_pk_service,\
    modify_author_service, delete_author_service


class ListCreateAuthors(Controller):
    def get(self, request):
        """
        List all authors
        :param request:
        :return:
        """

        ok, result, errors = get_all_authors_service()
        if errors:
            return BadRequest(errors)
        return Ok({'authors': [u.toJSONDict() for u in result['users']]})

    def post(self, request):
        """
        Create author
        :param request:
        :return:
        """
        data = request['body']
        created, author, errors = create_author_service(**data)
        if errors:
            return BadRequest(errors)
        return Ok({'author': [author.toJSONDict()]})


class DetailUpdateDeleteAuthor(Controller):
    def get(self, request):
        author_pk = request.get('uri')
        if not author_pk:
            return BadRequest({'msg': "No pk"})

        g, author, errors = get_author_by_pk_service(author_pk)
        if errors:
            return BadRequest(errors)
        return Ok({'author': [author.toJSONDict()]})

    def patch(self, request):
        author_pk = request.get('uri')
        if not author_pk:
            return BadRequest({'msg': "No pk"})
        data = request['body']

        modified, author, errors = modify_author_service(author_pk, **data)
        if errors:
            return BadRequest(errors)
        return Ok({'author': [author.toJSONDict()]})

    def delete(self, request):
        author_pk = request.get('uri')
        if not author_pk:
            return BadRequest({'msg': "No pk"})
        deleted, author, errors = delete_author_service(author_pk)
        if errors:
            return BadRequest(errors)
        return Ok({'msg': "deleted"})



