tabela = [['maças', 'laranjas', 'cerejas', 'bananas'],
          ['Alice', 'Bob', 'Carol', 'David'],
          ['Cachorro', 'gatos', 'ratos', 'seila']]

def mostrarTabela(table):
    largura = 0 

    for linha in table:
        for item in linha:
            if len(item) > largura:
                largura = len(item)

    for linha in table:
        for item in linha:
            print(item.rjust(largura), end="  ")
        print()

mostrarTabela(tabela)
