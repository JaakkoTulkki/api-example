from .entity import Entity

class Author(Entity):
    def __init__(self, first_name, last_name, date_of_birth=None, date_of_death=None):
        self.first_name = first_name
        self.last_name = last_name
        if date_of_birth:
            self.date_of_birth = date_of_birth.strftime('%d-%m-%Y')
        if date_of_death:
            self.date_of_birth = date_of_death.strftime('%d-%m-%Y')

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def toJSONDict(self):
        l = ['first_name', 'last_name']
        for i in ['date_of_birth', 'date_of_death']:
            if hasattr(self, i):
                l.append(i)
        return super().toJSONDict(l)
