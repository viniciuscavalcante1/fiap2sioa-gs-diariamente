class Usuario:
    """Representa um usuário no sistema.

    Attributes:
        nome (str): Nome do usuário.
        email (str): E-mail do usuário.
        senha (str): Senha do usuário.
    """

    def __init__(self, nome, email, senha):
        """Inicializa um novo objeto de usuário.

            Args:
                nome (str): Nome do usuário.
                email (str): E-mail do usuário.
                senha (str): Senha do usuário.
        """
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        """Retorna uma representação de string do objeto usuário."""
        return f"Usuário: {self.nome}\nE-mail: {self.email}"

    def __lt__(self, other):
        """Verifica se o e-mail deste usuário é menor que o e-mail de outro usuário."""
        return self.email < other.email

    def __le__(self, other):
        """Verifica se o e-mail deste usuário é menor ou igual ao e-mail de outro usuário."""
        return self.email <= other.email

    def __eq__(self, other):
        """Verifica se o e-mail deste usuário é igual ao e-mail de outro usuário."""
        return self.email == other.email

    def __ne__(self, other):
        """Verifica se o e-mail deste usuário é diferente do e-mail de outro usuário."""
        return self.email != other.email

    def __gt__(self, other):
        """Verifica se o e-mail deste usuário é maior que o e-mail de outro usuário."""
        return self.email > other.email

    def __ge__(self, other):
        """Verifica se o e-mail deste usuário é maior ou igual ao e-mail de outro usuário."""
        return self.email >= other.email

    def dict(self):
        """Retorna um dicionário representando as informações do usuário."""
        return {"email": self.email, "nome": self.nome, "senha": self.senha}
