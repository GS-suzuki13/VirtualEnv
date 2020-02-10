from Person.Dao.BaseDao import BaseDao
from Person.Model.PersonModel import PersonModel


class PersonDao(BaseDao):
    def __init__(self, model):
        super().__init__(model)