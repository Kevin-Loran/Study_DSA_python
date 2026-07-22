import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype=int)

    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} - {self.vetor[i]}")

    #O(1) - O(2)
    def insercao(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print("A capacidade maxima foi atingida.")
        else:
            self.ultima_posicao += 1
            self.vetor[self.ultima_posicao] = valor

    #O(n)
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.vetor[i] == valor:
                return i
        return -1

vetor = VetorNaoOrdenado(5)
vetor.insercao(4)
vetor.insercao(3)
vetor.insercao(2)
vetor.insercao(1)
vetor.insercao(0)

vetor.imprime()
print(f"\nposição do valor: {vetor.pesquisa(2)}")