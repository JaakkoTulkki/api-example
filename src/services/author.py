from entities.author import Author

from repositories.author import create_author, delete_author, get_all_authors, \
    get_author_by_name, get_author_by_pk, update_author

def create_author_service(first_name, last_name, date_of_birth=None, date_of_death=None):
    if not get_author_by_name(first_name, last_name).first():
        author = create_author(first_name=first_name, last_name=last_name, birth_date=date_of_birth,
                      date_of_death=date_of_death)
        author = Author(pk=author.id, first_name=author.first_name, last_name=author.last_name,
                        date_of_birth=author.birth_date, date_of_death=author.date_of_death)
        return True, author, None
    else:
        return False, None, {'msg': "Author exists already"}

def get_all_authors_service():
    return True, get_all_authors(), None


def modify_author_service(author_pk, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
    author = get_author_by_pk(author_pk).first()
    if not author:
        return False, None, {'msg': "Author does not exist"}
    author = update_author(author, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                  date_of_death=date_of_death)

    author = Author(pk=author.id, first_name=author.first_name, last_name=author.last_name,
                        date_of_birth=author.birth_date, date_of_death=author.date_of_death)
    return True, author, None


def get_author_by_pk_service(pk):
    got_it, author, errors = modify_author_service(author_pk=pk)
    if got_it:
        return True, author, None
    return False, None, {'msg': "Did not find the author"}


def delete_author_service(pk):
    deleted = delete_author(pk)
    if not deleted:
        return False, None, {'msg': "Author does not exist"}
    return True, None, None


