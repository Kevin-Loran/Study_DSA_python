alunos = {"pedro": 8.0, "Maria": 10.0, "Amilton": 7.5}


with open("Dados.txt", "w") as arquivo:
    for aluno, notas in alunos.items():
        arquivo.writelines(f"{aluno}: {notas}\n")

with open("Dados.txt", "r") as texto:
    for linhas in texto:
        print(linhas)