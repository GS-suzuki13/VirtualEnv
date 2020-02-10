from flask_restful import Resource
from flask import request,json

from Person.Dao.BaseDao import BaseDao

class BaseController(Resource):
    def __init__(self, model):
        self.db = BaseDao(model)

    def get(self, id=None):
        if id:
            return self.db.select_by_id(id)
        return self.db.select_all()

    def delete(self, id):
        return self.db.delete(id)

    def post(self, model):
        return self.db.insert(model)

    def put(self, model):
        return self.db.update(model)

    def getDados(self):
        kwargs = {}
        for key, value in request.json.items():
            kwargs[key] = value

        return kwargs