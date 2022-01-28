# здесь контроллеры/хендлеры/представления для обработки запросов
# (flask ручки). сюда импортируются сервисы из пакета service


from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):  # получить все фильмы по фильтрам
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):  # создать фильм
        read_json = request.json
        movie_service.create(read_json)

        return "", 201,


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):  # получить фильм по id
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def delete(self, mid: int):  # удалить фильм
        movie_service.delete(mid)
        return '', 204

    def put(self, mid: int):  # изменить информацию о фильме
        read_json = request.json
        read_json['id'] = mid
        movie_service.update(read_json)

        return '', 204
