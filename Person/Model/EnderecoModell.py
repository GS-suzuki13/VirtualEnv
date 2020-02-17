from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class PersonModel(Base):
    __tablename__ = "Person"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(length=100))
    Age = Column(Integer)
    Sex = Column(String(length=20))

    def __init__(self, Name, Age, Sex, ID=None):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.Sex = Sex

    def serialize(self):
        return {
            "ID" : self.ID,
            "Name" : self.Name,
            "Age" : self.Age,
            "Sex" : self.Sex
        }