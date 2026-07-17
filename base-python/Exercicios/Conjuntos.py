#remoção de duplicatas:
ids_registrados = [102, 105, 101, 102, 108, 105, 110, 101, 120]
idsUnicos = set(ids_registrados)
contador = 0
for ids in idsUnicos:
    contador += 1
    print(f"id{contador}: {ids}")

#intersection:
interesesDoArthur = {"futebol", "cinema", "livros", "viagem", "games" }
interesesDaBeatriz = {"teatro", "livros", "musica", "viagem", "astronomia" }
matchIntereses = interesesDaBeatriz.intersection(interesesDoArthur)

print(f"\ninteresses em comum: {matchIntereses}")

#difference:
alunosMatriculados = {"ana", "bruno", "carlos", "diego", "eduardo", "fernanda"}
alunosPresentes = {"bruno", "eduardo", "fernanda"}
alunosNaoPresentes = alunosMatriculados.difference(alunosPresentes)

print(f"\nos alunos que faltaram foram: {alunosNaoPresentes}")

#symmetric_difference:
listaA = {"srv-web1", "srv-db", "srv-auth", "srv-cache"} #servidores de semana passada
listaB = {"srv-web1", "srv-db", "srv-api", "srv-storage"} #servidores dessa semana
servidoresAlterados = listaA.symmetric_difference(listaB)

print(f"\nservidores que sofreram alterações[desativados/novos]: {servidoresAlterados}")
