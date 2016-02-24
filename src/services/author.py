from entities.author import Author

from repositories.author import create_author, get_author_by_name

def create_author_service(first_name, last_name, date_of_birth=None, date_of_death=None):
    if not get_author_by_name(first_name, last_name).first():
        author = create_author(first_name=first_name, last_name=last_name, birth_date=date_of_birth,
                      date_of_death=date_of_death)
        author = Author(first_name=author.first_name, last_name=author.last_name,
                        date_of_birth=author.birth_date, date_of_death=author.date_of_death)
        return True, author, None
    else:
        return False, None, {'msg': "Author exists already"}


