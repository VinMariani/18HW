from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid): # получить по id
        return self.session.query(Genre).get(gid)

    def get_all(self): # получить все жанры
        return self.session.query(Genre).all()

    #def create(self, data):
        #genre = Genre(**data)

        #self.session.add(genre)
        #self.session.commit()

        #return genre

    #def update(self, genre):
        #self.session.add(genre)
        #self.session.commit()

        #return '', 204

    #def delete(self, gid):
        #genre = self.get_one(gid)

        #self.session.delete(genre)
        #self.session.commit()

        #return '', 204