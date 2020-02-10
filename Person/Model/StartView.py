from flask import Flask
from flask_restful import Api

from Person.Controller.PersonController import PersonController

app = Flask(__name__)
api = Api(app)

api.add_resource(PersonController, "/api/Person", endpoint="persons")
api.add_resource(PersonController, "/api/Person/<int:id>", endpoint="person")

app.run(debug=True)