# это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid): # получить фильм по id
        return self.session.query(Movie).get(mid)

    def get_all(self): # получить все фильмы
        return self.session.query(Movie).all()

    def create(self, data): # создать фильм
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie): # изменить информацию о фильме
        self.session.add(movie)
        self.session.commit()

        return '', 204

    def delete(self, mid): # удалить фильм
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

        return '', 204