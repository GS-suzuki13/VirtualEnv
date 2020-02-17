from Comment.Dao.Comment_Dao import CommentDao
from flask_restful import Resource


class Comment_Controller(Resource):

    def __init__(self):
        self.dao = CommentDao()

    def get(self):
        return self.dao.list_all()