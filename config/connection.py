from pymongo import MongoClient



class Connection:
    def __init__(self, database):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client[database]

    # SELECT id, nombre FROM usuarios WHERE id = 1 AND rol_id > 1
    # collection = usuarios
    # condition => { id: { $eq: 1 }, rol_id: { $gt: 1 } }
    # select => { id: 1, nombre: 1 }
    def get_all(self, collection, condition={}, select={}):
        collect = self.db[collection]
        return collect.find(condition, select)

    def get_one(self, collection, condition={}, select={}):
        collect = self.db[collection]
        return collect.find_one(condition, select)

    # collection = alumnos
    # data => { nombre: 'Carlos', edad: 12, dni: 99999999 }
    def insert(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_one(data)
        print(f'Insert ID -> {result.inserted_id}')

    # collection = alumnos
    # data => [{ nombre: 'Carlos', edad: 12, dni: 99999999 }, {....}]
    def insert_many(self, collection, data):
        collect = self.db[collection]
        result = collect.insert_many(data)
        print(f'Insert IDs -> {result.inserted_ids}')

    def update(self, collection, condition, change):
        collect = self.db[collection]
        collect.update_one(condition, {
            '$set': change
        })
        print('Updated Document')

    def update_many(self, collection, condition, change):
        collect = self.db[collection]
        result = collect.update_many(condition, {
            '$set': change
        })
        print(f'Updated Document -> {result.raw_result} - Match {result.matched_count}')

    def delete(self, collection, condition):
        collect = self.db[collection]
        collect.delete_one(condition)
        print(f'Delete Document')

    # collection = alumnos
    def delete_many(self, collection, condition):
        collect = self.db[collection]
        result = collect.delete_many(condition)
        print(f'Delete Documents -> {result.deleted_count}')
