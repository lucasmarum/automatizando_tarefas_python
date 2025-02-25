def collatz(num):
    if num % 2 == 0:
        num = num // 2
        print(num)
    else:
        num = 3 * num + 1
        print(num)
    return num

print('Digite um número: ')
numero_usuario = int(input())

while numero_usuario != 1:
    numero_usuario = collatz(numero_usuario)
