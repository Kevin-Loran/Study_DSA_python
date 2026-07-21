import re

# Extrair números de telefone:
numero = "O meu numero de telefone é: (11)98765-4321."
print(re.search(r'\(\d{2}\)\d{5}\-\d{4}' ,numero))


# Extrair URLs:
url = " essa URL: https://www.exemplo.com.br/artigos?id=123 é do meu novo site."
print(re.search('https?://[A-Za-z0-9./]+' ,url))


# Extrair cep:
cep = "01001-000 é o meu cep."
padrao = r'\d+-\d{3}'
print(re.search(padrao,cep))
