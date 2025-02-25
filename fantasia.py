inventario = {'corda': 1, 'flechas': 12, 'Moeda de ouro': 42, 'tochas': 6}
lootDragao = ['Moeda de ouro', 'corda', 'Moeda de ouro', 'rubi', 'flecha']

def mostrarInventario(qinventario):
    total = 0
    for k, v in qinventario.items():
        print(k + ' ' + str(v))
        total = total + v
    print('Numero total de itens: ' + str(total))

def adicionarInventario(qinventario, itens_adicionados):
    for item in itens_adicionados:
        if item in qinventario:
            qinventario[item] += 1
        else:
            qinventario[item] = 1

mostrarInventario(inventario)
adicionarInventario(inventario, lootDragao)
print("Inventário atualizado:")
mostrarInventario(inventario)
