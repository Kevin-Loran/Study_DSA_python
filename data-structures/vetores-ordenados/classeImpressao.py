import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype=int)


    def impressao(self):
        for i in range(self.vetor):
            print(f"{i} - {self.vetor[i]}")

vetor = VetorOrdenado(5)

