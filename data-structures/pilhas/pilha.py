import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__pilha = np.empty(capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            return print("Pilha cheia")
        else:
            self.__topo += 1
            self.__pilha[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            return print("Pilha vazia")
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__pilha_vazia():
            return print("Pilha vazia")
        else:
            return print(self.__pilha[self.__topo])



pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)
pilha.ver_topo()