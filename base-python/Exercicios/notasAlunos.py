print("Digite as notas M1, M2 e M3 do aluno:")
m1 = float(input("M1: "))
m2 = float(input("M2: "))
m3 = float(input("M3: "))

media = float((m1 + m2 + m3)/ 3)

if ( media <= 4):
    print("voce foi reprovado.")
elif ( media >= 4.1 and media <= 6):
    print("voce foi aprovado para o exame.")
    m4 = float(input("M4: "))
    if ( m4 > 6):
        print("voce foi aprovado.")
    else:
        print("voce foi reprovado.")
elif media > 6:
    print("voce foi aprovado. :D")
else:
    print("notas invalidas.")