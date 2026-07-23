import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype=int)
        
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return "valor não existente."
        x = posicao
        while x < self.ultima_posicao:
            self.vetor[x] = self.vetor[x + 1]
            x += 1
        self.ultima_posicao -= 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.vetor[i] == valor:
                return i
        return -1

    def insercao(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade do vetor atingida!!")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.vetor[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.vetor[x + 1] = self.vetor[x]
            x -= 1
        self.vetor[posicao] = valor
        self.ultima_posicao += 1


    def impressao(self):
        for i in range(self.ultima_posicao + 1):
            print(f"{i} - {self.vetor[i]}")

vetor = VetorOrdenado(5)
vetor.insercao(2)
vetor.insercao(3)
vetor.insercao(1)
vetor.insercao(4)
vetor.excluir(3)
vetor.impressao()

