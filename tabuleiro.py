tabuleiro = {'TOP-L': ' ', 'TOP-M' : ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M' : ' ', 'MID-R': ' ',
            'LOW-L': ' ', 'LOW-M' : ' ', 'LOW-R': ' '}
def printTabuleiro(otabuleiro):
    print(tabuleiro['TOP-L'] + '|' + tabuleiro['TOP-M'] + '|' + tabuleiro['TOP-R'])
    print('-+-+-')
    print(tabuleiro['MID-L'] + '|' + tabuleiro['MID-M'] + '|' + tabuleiro['MID-R'])
    print('-+-+-')
    print(tabuleiro['LOW-L'] + '|' + tabuleiro['LOW-M'] + '|' + tabuleiro['LOW-R'])

turno = 'X'
for i in range(9):
    printTabuleiro(tabuleiro)
    print('Turno do: ' + turno + ' Qual casa deseja ocupar? ')
    movimento = input()
    tabuleiro[movimento] = turno
    if turno == 'X':
        turno = 'O'
    else:
        turno = 'X'
printTabuleiro(tabuleiro)