from Person.Dao.BaseDao import BaseDao


class PersonDao(BaseDao):
    def __init__(self, model):
        super().__init__(model)