from Dao.Comment_Dao import CommentDao
from flask_restful import Resource
from Model.Comment import Comment
from flask import request


class Comment_Controller(Resource):

    def __init__(self):
        self.dao = CommentDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        model = self.carrega_param()
        return self.dao.create(model)

    def delete(self, id):
        return self.dao.delete(id)

    def carrega_param(self):
        id = request.json['id']
        pessoa_id = request.json['pessoa_id']
        post_id = request.json['post_id']
        conteudo = request.json['conteudo']
        post_id = request.json['post_id']
        dt_envio = request.json['dt_envio']
        model = Comment(pessoa_id, post_id, conteudo, conteudo, id)
        return model
