
from flask_restful import Api
from flask import Flask

from Controller.Comment_Controller import Comment_Controller

app = Flask(__name__)
api = Api(app)

api.add_resource(Comment_Controller, '/api/comment/<int:id>', endpoint='comentario')
api.add_resource(Comment_Controller, '/api/comment', endpoint='comentarios')

app.run(debug=True)