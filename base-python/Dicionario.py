dadosCadastro = {
    "nome": ("seu nome", str),
    "sobrenome": ("seu sobrenome", str),
    "idade": ("sua idade", int),
    "altura": ("sua altura", float),
}

listaDeCompras = {
    "doces": ["chocolates, balas, bolos, brigadeiros"],
    "itemDelimpeza": "Detergente",
    "churrasco": ["picanha", "alcatra", "coxãoMole"]
}

print("\nPreencha com seus dados: ")

for dados in dadosCadastro:
    dadosCadastro[dados] = input(f"escreve seu/sua {dados}: ").strip()

print("\nDados coletados: ")
for dados in dadosCadastro:
    print(dadosCadastro[dados])

for itens, Compras in listaDeCompras.items():
    print(f"Itens:{itens} -- O que comprar: {Compras}")