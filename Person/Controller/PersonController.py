from Person.Model.PersonModel import PersonModel
from Person.Controller.BaseController import BaseController


class PersonController(BaseController):
    def __init__(self):
        super().__init__(PersonModel)

    def post(self):
        return super().post(PersonModel(**super().getDados()))

    def put(self, id):
        dic = super().getDados()
        dic[id] = id
        super().put(PersonModel(**dic))