aniversarios = {'Alice' : '1 ABRIL', 'Bob': '12 Dezembro', 'Carol': '4 MARÇO'}
while True:
    print('Digite um nome: (ENTER para sair)')
    nome = input()
    if nome == '':
        break
    if nome in aniversarios:
        print(aniversarios[nome] + ' é o aniversario de: ' + nome)
    else:
        print('Eu nao tenho informações sobre: ' + nome)
        print('Quando é o aniversario dele?')
        dia = input()
        aniversarios[nome] = dia
        print('BASE DE DADOS ATUALIZADA :)')