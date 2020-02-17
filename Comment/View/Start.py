from flask_restful import Api
from flask import Flask

from Comment.Controller.Comment_Controller import Comment_Controller

app = Flask(__name__)
api = Api(app)

api.add_resource(Comment_Controller, '/api/comment', endpoint='comentario')

app.run(debug=True)