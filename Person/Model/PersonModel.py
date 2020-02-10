from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class PersonModel(Base):
    __tablename__ = "Person"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    Age = Column(Integer)
    Sex = Column(String(20))

    def __init__(self, name, age, sex, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "sex" : self.sex
        }