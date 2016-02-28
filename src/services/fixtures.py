import datetime

from repositories.session import session_manager
from repositories.user import create_user
from repositories.author import create_author
from repositories.book import create_book, create_tag, modify_book


def load_fixtures():
    session_manager.create_session()

    _load_users_fixtures()

    session_manager.commit_session()
    session_manager.close_session()


def _load_users_fixtures():
    create_user('jimena@test.com', 'abc12345', '8c99f50fcb424c66b6e489d15461b782')
    create_user('nikolai@test.com', 'abc12345', '9942eb5913c54f2eae5353e6b43324fb')

    e = create_author("Ernest", "Hemingway", datetime.date(1899, 3, 20), datetime.date(1950, 6, 7))
    d = create_author("Fjodor", "Dostoyevski", datetime.date(1800, 3, 30), datetime.date(1876, 1, 11))

    bells = create_book(e, "To Whom the Bell Toll")
    man = create_book(e, "Man and the Sea")

    crime = create_book(d, "Crime and Punishment")
    gambler = create_book(d, "The Gambler")

    t, crime_tag = create_tag("crime")
    t, classic_tag = create_tag("classic")

    modify_book(bells.id, None, None, [crime_tag.id, classic_tag.id])

    modify_book(man.id, None, None, [crime_tag.id, classic_tag.id])
    modify_book(crime.id, None, None, [crime_tag.id, classic_tag.id])

    modify_book(gambler.id, None, None, [crime_tag.id])
    modify_book(gambler.id, None, None, [classic_tag.id])



