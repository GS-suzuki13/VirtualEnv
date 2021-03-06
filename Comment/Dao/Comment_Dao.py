
from Model.Comment import Comment


class CommentDao:

    def chamar_arquivo(self, metodo):
        self.arquivo = open(r'C:\Users\900164\Documents\VirtualEnv\Comment\Comment.txt', metodo)

    def create(self, comment: Comment, metodo='a'):
        self.chamar_arquivo(metodo)
        string = comment.__str__()
        self.arquivo.write(string)
        self.arquivo.close()
        return comment.as_dict()

    def buscar_classe(self, classes, id):
        for classe in classes:
            classe_dict = classe.as_dict()
            if int(classe_dict['id']) == id:
                return classe

        return None

    def atualizar_arquivo(self, classes):
        self.chamar_arquivo('w')
        for classe in classes:
            string = classe.__str__()
            self.arquivo.write(string)

        self.arquivo.close()

    def delete(self, id):
        classes = self.get_dados()
        classe = self.buscar_classe(classes, id)
        if classe is None:
            return 'Objeto não encontrado'

        else:
            classes.remove(classe)
            self.atualizar_arquivo(classes)
            return 'Objeto deletado'

    def get_by_id(self, id):
        classes = self.get_dados()
        classe = self.buscar_classe(classes, id)
        if classe is None:
            return 'Objeto não encontrado'

        else:
            return classe.as_dict()

    def get_dados(self):
        self.chamar_arquivo('r')
        lista = self.arquivo.readlines()
        classes = []
        for dado in lista:
            dado = dado.strip().split(';')
            classe = Comment(dado[0], dado[1], dado[2], dado[3], dado[4])
            classes.append(classe)

        self.arquivo.close()
        return classes

    def list_all(self):
        classes = self.get_dados()
        lista = []
        for classe in classes:
            lista.append(classe.as_dict())

        return lista

    def update(self, model):
        classes = self.get_dados()
        for classe in classes:
            classe_dict = classe.as_dict()
            if model.id == classe_dict['id']:
                classe.id = model.id
                classe.pessoa_id = model.pessoa_id
                classe.post_id = model.post_id
                classe.conteudo = model.conteudo
                classe.dt_envio = model.dt_envio

        self.atualizar_arquivo(classes)
        return classe.as_dict()
