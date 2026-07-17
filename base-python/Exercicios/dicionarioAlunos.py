lista_alunos = {}
total_alunos = 3

print("-- Cadastro de Alunos --")
for i in range(total_alunos):
    print(f"informe os dados do aluno{i+1}: ")
    nome = input("Nome: ").strip()
    while True:
        try:
            nota = float(input(f"Nota: "))
            break
        except ValueError:
            print("Digite uma nota válida(use o ponto para decimais)")
    lista_alunos[nome] = nota

todas_as_notas = []
for notas in lista_alunos.values():
    todas_as_notas.append(notas)

soma_notas = sum(todas_as_notas)
quantidade_notas = len(todas_as_notas)
media = soma_notas/quantidade_notas

print("\n" + "="*30)
print(f"A média das notas dos {quantidade_notas} é de: {media:.2f}")
print("="*30)

