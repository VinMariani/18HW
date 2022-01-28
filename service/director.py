from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did): # получение по id
        return self.dao.get_one(did)

    def get_all(self): # получение всех
        return self.dao.get_all()

    #def create(self, data):
        #return self.dao.create(data)

    #def update(self, data):
        # = data.get('id')
        #director = self.get_one(did)

        #director.id = data.get('id')
        #director.name = data.get('name')

        #self.dao.update(director)

    #def update_partial(self, data):
        #did = data.get('id')
        #director = self.get_one(did)

        #if 'id' in data:
            #director.id = data.get('id')
        #if 'name' in data:
            #director.name = data.get('name')

        #self.dao.update(director)

    #def delete(self, did):
        #self.dao.delete(did)