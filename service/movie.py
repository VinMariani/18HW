# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid): # получение фильма
        return self.dao.get_one(mid)

    def get_all(self): # получение всех фильмов
        return self.dao.get_all()

    def create(self, data): # добавление всех фильмов
        return self.dao.create(data)

    def update(self, data): # изменение фильма
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')

        self.dao.update(movie)

    def update_partial(self, data): # частичное изменение фильма
        mid = data.get('id')
        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')

        self.dao.update(movie)

    def delete(self, mid): # удаление фильма
        self.dao.delete(mid)