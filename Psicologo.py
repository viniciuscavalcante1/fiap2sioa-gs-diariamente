import Pessoa


class Psicologo(Pessoa):
    def __init__(self, nome, senha, idade, email, especialidades, whatsapp):
        super().__init__(nome, senha)
        self.idade = idade
        self.email = email
        self.especialidades = especialidades
        self.whatsapp = whatsapp
