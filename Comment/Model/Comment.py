
class Comment():

    def __init__(self, pessoa_id, post_id, conteudo, dt_envio, id=None):
        self.id = id
        self.pessoa_id = pessoa_id
        self.post_id = post_id
        self.conteudo = conteudo
        self.dt_envio = dt_envio

    def __str__(self):
        return f'{self.pessoa_id};{self.post_id};{self.conteudo};{self.dt_envio};{self.id}\n'

    def as_dict(self):
        return {
            "id": self.id,
            "pessoa_id": self.pessoa_id,
            "post_id": self.post_id,
            "conteudo": self.conteudo,
            "dt_envio": str(self.dt_envio)
        }