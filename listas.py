catNames = []
while True:
    print('Insira o nome do gato ' + str(len(catNames) + 1) + ' (Ou nao digite nada para parar.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("Nome dos gatos: ")
for name in catNames:
    print(' ' + name)
