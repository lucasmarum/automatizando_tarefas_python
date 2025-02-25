import pprint
mensagem = 'Eu adoro python!! é minha linguagem preferida'
count = {}
for caractere in mensagem:
    count.setdefault(caractere, 0)
    count[caractere] = count[caractere] + 1
pprint.pprint(count)