import re
telefone_regex = re.compile(r'\d\d\d\d\d-\d\d\d\d')
numero_teste = telefone_regex.search(("meu numero de telefone é 95678-5367"))
print(numero_teste.group())