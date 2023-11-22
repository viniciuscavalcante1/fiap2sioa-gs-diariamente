from NoAVL import NoAVL
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.caminho_comparacoes = []

    def altura_avl(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento_avl(self, no):
        if not no:
            return 0
        return self.altura_avl(no.esquerda) - self.altura_avl(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura_avl(y.esquerda), self.altura_avl(y.direita))
        x.altura = 1 + max(self.altura_avl(x.esquerda), self.altura_avl(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T3 = y.esquerda

        y.esquerda = x
        x.direita = T3

        x.altura = 1 + max(self.altura_avl(x.esquerda), self.altura_avl(x.direita))
        y.altura = 1 + max(self.altura_avl(y.esquerda), self.altura_avl(y.direita))

        return y

    def inserir(self, no, dados):
        if not no:
            return NoAVL(dados)

        if dados < no.dados:
            no.esquerda = self.inserir(no.esquerda, dados)
        else:
            no.direita = self.inserir(no.direita, dados)

        no.altura = 1 + max(self.altura_avl(no.esquerda), self.altura_avl(no.direita))

        balance = self.fator_balanceamento_avl(no)

        if balance > 1:
            if dados < no.esquerda.dados:
                return self.rotacao_direita(no)
            else:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
                return self.rotacao_direita(no)

        if balance < -1:
            if dados > no.direita.dados:
                return self.rotacao_esquerda(no)
            else:
                no.direita = self.rotacao_direita(no.direita)
                return self.rotacao_esquerda(no)

        return no

    def inserir_dados(self, dados):
        self.raiz = self.inserir(self.raiz, dados)

    def contar_comparacoes(self, dados):
        self.caminho_comparacoes = []
        return self.buscar(self.raiz, dados, 1)

    def buscar(self, no, dados, comparacoes):
        if not no:
            return (None, comparacoes)

        self.caminho_comparacoes.append(no.dados)

        if dados == no.dados:
            return (no.dados, comparacoes)
        elif dados < no.dados:
            return self.buscar(no.esquerda, dados, comparacoes + 1)
        else:
            return self.buscar(no.direita, dados, comparacoes + 1)