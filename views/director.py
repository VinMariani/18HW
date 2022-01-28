from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('director')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self): # получение всех
        all_directors = director_service.get_all()

        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int): # получение по id
        director = director_service.get_one(did)

        return director_schema.dump(director), 200