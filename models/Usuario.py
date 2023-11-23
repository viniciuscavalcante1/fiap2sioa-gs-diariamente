class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Usuário: {self.nome}\nE-mail: {self.email}"

    def __lt__(self, other):
        return self.email < other.email

    def __le__(self, other):
        return self.email <= other.email

    def __eq__(self, other):
        return self.email == other.email

    def __ne__(self, other):
        return self.email != other.email

    def __gt__(self, other):
        return self.email > other.email

    def __ge__(self, other):
        return self.email >= other.email