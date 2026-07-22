import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i])

vetor = VetorNaoOrdenado(5)
vetor.imprime()
