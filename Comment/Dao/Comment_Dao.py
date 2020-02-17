from Comment.Model.Comment import Comment

class CommentDao:

    def chamar_arquivo(self, metodo):
        self.arquivo = open(r'C:\Users\900142\Desktop\VirtualEnv\Comment\Comment.txt', metodo)

    def create(self, comment: Comment, metodo='a'):
        self.chamar_arquivo(metodo)
        string = comment.__str__()
        self.arquivo.write(string)
        self.arquivo.close()

    def delete(self, id):
        comentario = self.list_all()
        comentarios = []
        for comment in comentario:
            if int(comment[4]) == id:
                comentario.remove(comment)
            else:
                comentarios.append(comment)

        print(comentarios)
        self.update(comentarios, 'w')

    def update(self, comment, metodo):
        for dado in comment:
            model = Comment(dado[1], dado[2], dado[3], dado[4], dado[0])
            self.create(model.__str__(), metodo)

    def list_all(self):
        self.chamar_arquivo('r')
        lista = self.arquivo.readlines()
        comentarios = []
        for dado in lista:
            dado = dado.strip().split(';')
            comentarios.append(dado)
        self.arquivo.close()
        return comentarios


if __name__ == '__main__':
    comment = CommentDao()
    model = Comment(0, 0, "ddddd", '111112', 3)
    comment.create(model)
    a = comment.delete(0)
    print(comment.list_all())
