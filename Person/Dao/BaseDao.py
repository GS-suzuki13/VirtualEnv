from Person.Dao.Connection import Connection

class BaseDao(Connection):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def delete(self, id):
        try:
            person = self.session.query(self.model).filter_by(id=id).first()
            self.session.delete(person)
            self.session.commit()
        except:
            return "Error"
        else:
            return "Successfully Delete"

    def insert(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        except:
            return "Error"
        else:
            return "Inserted With Successfully"

    def select_all(self):
        person = self.session.query(self.model).all()
        ret= []
        for p in person:
            ret.append(p.serialize())

    def select_by_id(self, id):
        person = self.session.query(self.model).filter_by(id=id).first
        return person.serialize()

    def update(self, new):
        try:
            self.session.merge(new)
            self.session.commit()
        except:
            return "Error"
        else:
            return "Successfully Updated"