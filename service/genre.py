from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid): # получение по id
        return self.dao.get_one(gid)

    def get_all(self): # получение всех
        return self.dao.get_all()

    #def create(self, data):
        #return self.dao.create(data)

    #def update(self, data):
        #gid = data.get('id')
        #genre = self.get_one(gid)

        #genre.id = data.get('id')
        #genre.name = data.get('name')

        #self.dao.update(genre)

    #def update_partial(self, data):
        #gid = data.get('id')
        #genre = self.get_one(gid)

        #if 'id' in data:
            #genre.id = data.get('id')
        #if 'name' in data:
            #genre.name = data.get('name')

        #self.dao.update(genre)

    #def delete(self, gid):
        #self.dao.delete(gid)