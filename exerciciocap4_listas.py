def separador(lista):
    for i in range(len(lista)):
        if i != (len(lista) - 1):
            print(lista[i], end=', ')
        else:
            print('and ' + str(lista[i]))


teste = ['oi', 'pao', 'bolo', 'copo']
teste2 = [1,2,3,4,5,6,7,8,9]
separador(teste)
separador(teste2)
