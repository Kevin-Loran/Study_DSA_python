class Aluno:
    def __init__(self,nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def mostraDados(self):
        return print(f"nome: {self.nome}"
                     f"\nnota1: {self.nota1}"
                     f"\nnota2: {self.nota2} \n")

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def resultado(self):
        nota = self.media()
        if nota > 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Jailson", 7.8, 8.2)

aluno1.mostraDados()
print(aluno1.resultado())
