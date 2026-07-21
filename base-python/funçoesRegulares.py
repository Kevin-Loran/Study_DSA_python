import re

frase1 = "Meu número é (55)0000-0000"
frase2 = "A placa que eu anotei do carro era FRT-1998"
frase_match = "FRT-1998 é placa que eu anotei do carro."
frase3 = "Entre em contato meu teste@gmail.com"

stringEmails = (" email 1: primeiro@gmail.com "
                "\n email 2: segundo@hotmail.com "
                "\n email 3: terceiro@personalizado.com")

print("\n" + "="*30)
print(re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase1))
print(frase1[13:26])
print("="*30)

print("\n" + "="*30)
print(re.search(r'\w+-\d{3,4}', frase2))
print(re.match(r'\w+-\d{3,4}', frase_match))
print(frase2[35:43])
print("="*30)

print("\n" + "="*30)
print(re.search(r'\w+\@\w+\.\w+', frase3))
print(frase3[21:36])
print("="*30)

print("\n" + "="*30)
print(re.findall(r'\w+\@\w+\.\w+', stringEmails))
print(frase3[21:36])
print("="*30)