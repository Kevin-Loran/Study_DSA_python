idade = int(input("Digite sua idade:"))

if idade < 12:
    print("CRIANÇA")
elif idade >= 13  and idade <= 17:
    print("ADOLESCENTE")
elif idade > 18:
    print("ADULTO")
else:
    print("Idade inválida")

